#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

from typing import Mapping, List, NamedTuple, Generator

from cmk.base.plugins.agent_based.agent_based_api.v1.type_defs import (
    DiscoveryResult,
    CheckResult,
    StringTable,
)

from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    register,
    Service,
    check_levels,
    Result,
    SNMPTree,
    contains,
    State,
    render,
    startswith,
    Metric,
)

class HuaweiHWCache(NamedTuple):
    cache_id: int
    cache_readutil: int
    cache_writeutil: int
    cache_mirror_writeutil: int
    cache_hitratio: int

def parse_huawei_storage_hwcache(string_table) -> HuaweiHWCache:
    #pp.pprint(string_table)
    return HuaweiHWCache(
        cache_id =  0,
        cache_readutil = 0,
        cache_writeutil = 0,
        cache_mirror_writeutil = 0,
        cache_hitratio = 0,
    )

def discovery_huawei_storage_hwcache(section) -> DiscoveryResult:
    for id, ru, wu, mwu, hr in section:
      yield Service(item=id)

def check_huawei_storage_hwcache(item, params, section) -> CheckResult:
    for id, ru, wu, mwu, hr in section:
      if item == id:
        yield Result(state=State.OK, summary="HWCache %s: ok"%item)
        yield Metric("read_utilization", int(ru))
        yield Metric("write_utilization", int(wu))
        yield Metric("mirror_write_utilization", int(mwu))
        yield Metric("hit_ratio", int(hr))

register.snmp_section(
    name = "huawei_storage_hwcache",
    #parse_function = parse_huawei_storage_hwcache,
    detect = startswith(".1.3.6.1.2.1.1.1.0", "ISM SNMP Agent"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.34774.4.1.21.7.1',
        oids = [
            '1',    # hwPerfCacheID
            '2',    # hwPerfCacheReadUtilization
            '3',    # hwPerfCacheWriteUtilization
            '4',    # hwPerfCacheMirrorWriteUtilization
            '5',    # hwPerfCacheHitRatio
        ],
    ),
)

register.check_plugin(
    name="huawei_storage_hwcache",
    service_name="HWCache %s",
    discovery_function=discovery_huawei_storage_hwcache,
    check_function=check_huawei_storage_hwcache,
    check_default_parameters={},
)

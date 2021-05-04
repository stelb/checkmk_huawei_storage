from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
)

metric_info["read_utilization"] = {
    "title": _("Read Utilization"),
    "unit": "%",
    "color": "11/a",
}
metric_info["write_utilization"] = {
    "title": _("Write Utilization"),
    "unit": "%",
    "color": "21/a",
}
metric_info["mirror_write_utilization"] = {
    "title": _("Mirror Write Utilization"),
    "unit": "%",
    "color": "31/a",
}
metric_info["hit_ratio"] = {
    "title": _("Hit Ratio"),
    "unit": "%",
    "color": "41/a",
}

graph_info["huawei_storage_hwcache"] = {
    "title": _("HW Cache Utilization"),
    "metrics": [
        ("read_utilization", "line"),
        ("write_utilization", "line"),
        ("mirror_write_utilization", "line"),
        ("hit_ratio", "line"),
    ],
}

#####################################################################
#                                                                   #
# /naqs_devices/PulseBlasterESRPro300/__init__.py                   #
#                                                                   #
#                                                                   #
#####################################################################
from labscript_devices import deprecated_import_alias


# For backwards compatibility with old experiment scripts:
PulseBlasterESRPro300 = deprecated_import_alias(
    "naqs_devices.PulseBlasterESRPro300.labscript_devices.PulseBlasterESRPro300")

__version__ = '0.1.0'
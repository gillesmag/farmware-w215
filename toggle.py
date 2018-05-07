#!/usr/bin/env python
'''Control D-link DSP-W215

Toggles D-link DSP-W215 on and off.
'''

from pyW215 import SmartPlug, ON, OFF
import farmware_tools

import os

farmware_name = "control-w215"

def get_env(key, type_=str):
    return type_(os.environ["{}_{}".format(farmware_name, key)])

def main():
    sp = SmartPlug(get_env("ip_address"), get_env("pin_code"))
    #farmware_tools.log("{} {}".format(get_env("ip_address"), get_env("pin_code")))

if __name__ == "__main__":
    main()

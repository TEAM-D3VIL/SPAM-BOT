import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5

def load_plugs(plugname):
    modules = Path(f"spambot/plugins/{plugname}.py")
    myfiles = f"spambot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["spambot.plugins." + plugname] = load
    print("D3vilSpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import spambot
import spambot.userNeeds
import spambot.help
import spambot.helpers.callbackQuery

print("\n\nD3vil Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        D3vilBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        D3vilBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        D3vilBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
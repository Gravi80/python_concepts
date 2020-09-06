from os import environ
import importlib
from dotenv import load_dotenv
import sys

load_dotenv()

config_environments = importlib.import_module(f"environment_configs.config").__all__
if environ.get('APP_SETTINGS') in config_environments:
    config = getattr(importlib.import_module(f"environment_configs.config"), environ.get('APP_SETTINGS'))
else:
    print(f"invalid APP_SETTINGS {environ.get('APP_SETTINGS')}. Allowed {config_environments}")
    sys.exit()

# python environ_config_test.py

from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()

# Project base directory
PROJECT_DIR = Path(__file__).resolve().parent
BASE_DIR = PROJECT_DIR.parent

# Set default values for environment variables if they are not set
env.read_env(BASE_DIR / ".env")


def env_to_enum(enum_cls, value):
    for x in enum_cls:
        if x.value == value:
            return x

    raise ImproperlyConfigured(
        f"Env value {repr(value)} could not be found in {repr(enum_cls)}"
    )

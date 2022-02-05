[![codecov](https://codecov.io/gh/DAtek/datek-app-utils/branch/master/graph/badge.svg?token=UR0G0I41LD)](https://codecov.io/gh/DAtek/datek-app-utils)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>

# Utilities for building applications.

## Contains:
- Config loading from environment
- Bootstrap for logging

## Examples: 
```python
import os

from datek_app_utils.env_config.base import BaseConfig

os.environ["COLOR"] = "RED"
os.environ["TEMPERATURE"] = "50"


class Config(BaseConfig):
    COLOR: str
    TEMPERATURE: int


assert Config.COLOR == "RED"
assert Config.TEMPERATURE == 50
```

The `Config` class casts the values automatically.
Moreover, you can test whether all the variables have been set or not.

```python
import os

from datek_app_utils.env_config.base import BaseConfig
from datek_app_utils.env_config.utils import validate_config
from datek_app_utils.env_config.errors import ValidationError

os.environ["COLOR"] = "RED"


class Config(BaseConfig):
    COLOR: str
    TEMPERATURE: int


try:
    validate_config(Config)
except ValidationError as error:
    for attribute_error in error.errors:
        print(attribute_error)

```
Output:
```
TEMPERATURE: Not set. Required type: <class 'int'>
```
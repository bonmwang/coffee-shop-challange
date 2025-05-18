# Shared test utilities
import pytest

# Common test fixtures could be defined here
__all__ = []# Explicit empty list prevents implicit imports

# Mark 'tests/' as a python package.
# Can hold shared test fixtures or utilities but this is optional though.
# Prevents namespace pollution by explicitly declaring __all__ as empty.
# Enables test modules to import each ither if needed.
import os
from contextlib import suppress

with suppress(RuntimeError):
    os.remove('somefile.txt')

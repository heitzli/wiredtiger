# setuptools' build backend requires a setup.py next to pyproject.toml; all
# build logic lives in setup_pip.py.
import os

_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup_pip.py')
exec(compile(open(_p).read(), _p, 'exec'),
     {'__file__': _p, '__name__': '__main__'})

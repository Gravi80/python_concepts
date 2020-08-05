Based on Python 3.7

```
conda create -n python_concepts python=3.7
source activate python_concepts
```
Or
[choosing python version](https://github.com/pyenv/pyenv#choosing-the-python-version)
```
curl https://pyenv.run | bash
pyenv install 3.7
pyenv local 3.7
pyenv versions
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt --index-url https://pypi.org/simple/
```

### Python
Compiler: https://github.com/python/cpython/blob/5f2df88b63e50d23914e97ec778861a52abdeaad/Python/compile.c
Interpreter: https://github.com/python/cpython/blob/bcda8f1d42a98d9022736dd52d855be8e220fe15/Python/ceval.c

Main Method: https://github.com/python/cpython/blob/master/Programs/python.c

decorators : wrapping functions

class decorators : wrapping classes [Applied to single class] [After class is created]

Metaclasses : Doing things with class hierarchies [Applied to the whole hierarchy] [Before class is created]


#### Importing modules
modules present in 'sys.modules' are automatically imported during initialization.

import statements in python doesn't execute code. The import statement brings a name into scope

```from module import func```

Give me access to the module and say
``` func = module.func ``` i.e it binds func


```import math ```
There is no execution of code, it brings the "math" module into the scope
by doing something like :
```
math = sys.modules['math']
```

**The execution of code happens as a side-effect only when python can't find a module in sys.modules**

### Packaging/Project
https://github.com/audreyr/cookiecutter

https://pipenv.readthedocs.io/en/latest/

https://pypi.org/classifiers/

https://choosealicense.com/

https://www.gitignore.io/

https://pypi.org/project/check-manifest/


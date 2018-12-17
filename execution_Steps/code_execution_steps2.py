print("\n########################## Code Execution ##########################")
from builtins import open
from os import path

# When you say "import my_module".
# Python goes and finds my_module.py Or
# finds a folder containing __init__.py which contains my_module.py

# Step 1
# Read the file
with open(f'{path.dirname(__file__)}/my_module.py') as f:
    source = f.read()
print(f"source={source!r}")

# Step 2
# Parse source and create AST  [Tokenisation + Parsing]
from ast import parse

ast = parse(source)  # Tokenises the source code and turns it into AST(abstract syntax tree)
print(f'tokens={ast!r}')
print(ast.body)  # has function and class definition
print(ast.body[0].body)  # body of function definition
print(ast.body[0].body[0].value)  # value that func returns, Binary operation
print(ast.body[0].body[0].value.left.id)  # Left side of binary openration is a Name=num1
print(ast.body[0].body[0].value.right.id)  # Right side of binary openration is a Name=num2

# Step 3
# Compile AST and construct code object
code = compile(ast, 'my_module.py', mode='exec')
print(f'code={code!r}')
print(code.co_code)  # Actual byte code
print(code.co_name)  # Name of function
print(code.co_names)  # Name of local vars
print(code.co_nlocals)  # Number of local vars
# from dis import dis
# dis(code)

# Step 4
# Executes the code object and create a namespace
namespace = {}  # creates a namespace
exec(code, namespace)
print(f'namespace={namespace.keys()}')


# Step 5
# Using namespace construct the module
# Module is an python object having name, lookup mechanism, ability to lookup contents inside
class mod:
    def __init__(self, name, bases, body):
        self.name, self.base = name, bases
        self.__dict__.update(body)


my_module = mod('my_module', (), namespace)
print(f'module={dir(my_module)!r}')
print(my_module.Demo)
print(my_module.add)

# Step 6
# Use module

print(my_module.add(2, 3))

print("\n########################## Class Construction ##########################")
# Step 1
body = '''def __init__(self,name):
    self.name = name
def bar(self):
    print(f"I am {self.name}")'''

# Step 2, create an empty class dictionary
clsdict = type.__prepare__('ClassName', (object,))
print(clsdict)
# Step 3, clsdict is populated with the body methods and attributes
exec(body, globals(), clsdict)
print(clsdict)
# Step 4, Class is constructed
ClassName = type('ClassName', (object,), clsdict)
cn = ClassName('some_name')
cn.bar()

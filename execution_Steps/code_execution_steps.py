# When python reads the source code, it first converts it to a stream of tokens
# python -m tokenize execution_Steps/my_module.py
import ast
import dis
import tokenize
from os import path

import astpretty

# Step 1: Tokenization  [Lexical]
with open(f'{path.dirname(__file__)}/my_module.py', 'rb') as f:
    for token in tokenize.tokenize(f.readline):
        print(token)
# OP : Operator
# INDENT, DEDENT : For Indentation
# start=(line, character), end=(line, character)

# Step 2: Turn the stream of tokens in to AST (Parse the tokens) [Parsing]
# AST : Abstract syntax tree is a representation of what will actually happen in a program
astpretty.pprint(ast.parse("1+2+3"), show_offsets=False)
astpretty.pprint(ast.parse("(1+2)+3"), show_offsets=False)
# The brackets around 1 and 2 are not represented in the AST. So the syntax is being extracted away
# We can't go back from the AST to the exact source code
# colon, white-space, tabs, brackets are abstracted

# ast module parse the Text and hadles tokenisation in one step
with open(f'{path.dirname(__file__)}/my_module.py') as f:
    tree = ast.parse(f.read())
print(tree)
print(tree._fields)
for node in tree.body:
    print(node.lineno, node)

print(ast.dump(tree))
astpretty.pprint(tree, show_offsets=False)

# Step 3: Compile the AST to bytecode [code-object]
filename = path.abspath('my_module.py')
print(filename)
code = compile(tree, filename=filename, mode='exec')
# filename : To tag the code-object to know that this is where it is coming from. Backtrace can use these info
print(code)
print(dis.code_info(code))
# A tuple of constants. All constants are put in a tuple and are referred by an index
# Names : Tuple containing Names of the variable

# dis module hides few more attributes from us
for attr_name in dir(code):
    if not attr_name.startswith('__'):
        print(f'{attr_name}: {getattr(code,attr_name)}')
# co_code : Actual instructions that python will execute as code runs
# co_lnotab : Mapping of bytecode to line numbers
print(list(b for b in code.co_code))
print(dis.dis(code))
# python -m dis execution_Steps/my_module.py
print(dis.code_info(code.co_consts[2]))

# Step 4: Parsing is an expensive operation python will save/cache this. So, that next time when
# same module is loaded it doesn't have to parse it again [Serialization]
import marshal  # specially design for python code objects and can only serialize immutable types(Tuples, Numbers)

marshelled = marshal.dumps(code)
print(marshal.loads(marshelled))
print(list(marshelled))
# python put this marshelled/serialized code object in a .pyc file along with a header(first 16 bytes) for validating cache
# In .pyc file the first 4 bytes are the magic numbers. Same for every python version
# This tells python that this is the .pyc file for this particular version of the byte-code
import importlib.util

print(importlib.util.MAGIC_NUMBER)
print(list(importlib.util.MAGIC_NUMBER))
# Step 4: A code object is something that python can run
# exec(code)

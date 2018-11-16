from dataclasses import dataclass, field, fields
from datetime import datetime
from pprint import pprint


# https://www.python.org/dev/peps/pep-0557/
# https://docs.python.org/3/library/dataclasses.html

#  init => __init__() method will be generated
#  repr => __repr__() method will be generated
#  eq   => __eq__() method will be generated
# order =>  __lt__(), __le__(), __gt__(), and __ge__() methods will be generated
# unsafe_hash = False => a __hash__() method is generated
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Account:
    id: int
    owner: str
    valid_till: datetime = datetime.strptime('12122050', "%d%m%Y").date()


ac1 = Account(1, 'ravi')

from dataclasses import asdict, astuple, replace

ac1.owner = 'sample'
asdict(ac1)
astuple(ac1)
updated_ac1 = replace(ac1, owner='demo')


# Default -> Mutable, UnHashable (can't be used as dict key), Non-iterable, UnSortable
# These defaults are easily overriden by specifying that you want Immutabililty, hashability and ordering
# @dataclass(order=True, frozen=True)


@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: int = field()
    gender: int = field()
    salary: int = field(hash=False, repr=False, metadata={'units': 'bitcoin'})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append((viewer_id, datetime.now()))


e1 = Employee(emp_id='123', name='Emp1', gender='Female', salary=10, age=10)
e2 = Employee(emp_id='124', name='Emp2', gender='Male', salary=5, age=20)

pprint(sorted([e1,e2]))

fields(e1)
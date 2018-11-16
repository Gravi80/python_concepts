from typing import NamedTuple
from datetime import datetime

# Hashable, Iterable, Sortable
class Account(NamedTuple):
    id: int
    owner: str
    valid_till: datetime = datetime.strptime('12122050', "%d%m%Y").date()


ac1 = Account(1, 'ravi')

ac1._asdict()
tuple(ac1)
updated_ac1 = ac1._replace(owner='demo')  # _replace is not a private method

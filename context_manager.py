from contextlib import contextmanager
from sqlite3 import connect


@contextmanager
def temptable(cur):
    cur.execute('create table temp(x int,y int);')
    yield
    cur.execute('drop table temp;')


with  connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        for x, y in zip(range(10), range(10, 20)):
            cur.execute('insert into temp(x,y) values(?,?);', (x, y))
        for row in cur.execute('select * from temp;'):
            print(row)

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    t = Task('start server', 'mahmoods')    
    assert t.summary == 'start server'
    assert t.owner == 'mahmoods'
    assert t.done == False and t.id == None
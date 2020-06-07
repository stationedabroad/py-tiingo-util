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

def test_asdict():
    t_task = Task('reset server', 'mahmoods', True, 212)    
    d_task = t_task._asdict()
    expected = {
        'summary': 'reset server',
        'owner': 'mahmoods',
        'done': True,
        'id': 212
    }
    assert d_task == expected
from gevent import joinall, spawn, sleep


def foo():
    print('Running in foo')
    sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    sleep(0)
    print('Implicit context switch back to bar')


def foobar():
    joinall([
        spawn(foo),
        spawn(bar),
    ])

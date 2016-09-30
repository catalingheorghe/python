import threading
from time import sleep
from functools import wraps

class runner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        a = 1
        while a < 3:
            print('%s running' % threading.current_thread())
            a = a + 1
            sleep(1)

    def stop(self):
        pass

    def who(self):
        print(repr(self))

def testdeco(func):
    def new(*args, **kwargs):
        result = func(*args, **kwargs)
        print()
        for thread in threading.enumerate():
            print(thread)
        print()
        return result
    return new

def argdeco(arg):
    def threaddeco(func):
        @wraps(func)
        def new(*args, **kwargs):
            result = func(*args, **kwargs)
            for thread in threading.enumerate():
                print(arg, thread.name)
                if thread.__class__.__name__.startswith(arg):
                    print("this thread will be stopped: ", thread)
                    thread.stop()
            return result
        return new
    return threaddeco

@argdeco("runner")
def runthread():
    th = runner()
    
    th.start()
    return True

runthread()

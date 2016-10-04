import functools
def log(text=None):
    def decorator(func):
        if text==None:
            print('call %s()'%func.__name__)

        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('Begincall')
            f=func(*args,**kw)
            print('Endcall')
            return f
        return wrapper
    return decorator

@log('练习')
def now():
    print('被调用')

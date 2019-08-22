
x = 10

def set_val(a):
    global x; x = a

def get_val():
    print('GV: Module X')
    return x

__all__ = ('set_val',)

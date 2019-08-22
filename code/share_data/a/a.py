
x = 10

def set_val(a):
    global x; x = a

def get_val():
    return x

def globs():
    return globals().keys()

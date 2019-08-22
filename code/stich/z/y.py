import z.x

def get_val():
    print('GV: Module Y')
    return z.x.get_val()

__all__ = ('get_val',)

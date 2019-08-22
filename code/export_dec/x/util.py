from collections import defaultdict

exports = defaultdict(lambda: [])


def export(func):
    
    print('Exporting', func.__name__)
    exports[func.__module__].append(func.__name__)
    globals()[func.__name__] = func
    return func

def get_exports(module):
    return exports[module]

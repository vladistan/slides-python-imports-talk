import types
import sys


# This is custom import function.  It replicates what actual
# import statement does.  For simplicity it implements a bare
# minimum functionality


def import_module(modname):

    # Let's see if the module already loaded, return reference to it if
    # this is the case
    if modname in sys.modules:
        return sys.modules[modname]

    # Let's load from known location
    source_path = f"../share_data/{modname}/{modname}.py"

    # Open and read the module's source code
    with open(source_path, 'r') as f:
        code = f.read()

    # Create a module and compile the source
    mod = types.ModuleType(modname)
    code = compile(code, source_path, 'exec')

    # Add reference to this module to sys.modules
    sys.modules[modname] = mod
    exec(code, mod.__dict__)

    # Return module ref
    return sys.modules[modname]


# Stop here for exploration
import pdb; pdb.set_trace()

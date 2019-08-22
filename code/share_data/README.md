# Modules are loaded only once

Modules are loaded only once.  Subsequent 'import' statements just return the
module reference from the 'sys.modules'.  Since it's the same module,  it's possible
to share data between different components that import our module

![demo](https://github.com/vladistan/slides-python-imports-talk/blob/master/images/stitch_tty_demo.gif)

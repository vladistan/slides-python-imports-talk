# Auto installer

This is a silly `sys.meta_path` hook that pip installs missing modules.

Try creating empty virtual environment and running this.

Once prompted with (pdb) prompt, try importing various modules.

Note, this only works for the modules that have the same import name
and pip package name.


![demo](https://github.com/vladistan/slides-python-imports-talk/blob/master/images/auto_tty.gif)

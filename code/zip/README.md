# Fun with zips and directories

If directory contains a `__main__.py` file, it could be run either as script
or as a module.   Zip file of such directory is also a executable python
file.  Concatenating shebang stub with the zip file creates a self contained
executable python module.

![demo](https://github.com/vladistan/slides-python-imports-talk/blob/master/images/fun_with_zip_tty.gif)

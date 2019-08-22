# Stitching submodules

When writing larger library like Numpy or Pandas  it might be good to split it into multiple
submodules.  But, it is easier for the user to import just one library instead of a bunch of
separate modules.

That's where `__init__.py` comes handy.  We can use it to stitch stitch multiple modules
together.

![demo](https://github.com/vladistan/slides-python-imports-talk/blob/master/images/code_share_tty.gif)

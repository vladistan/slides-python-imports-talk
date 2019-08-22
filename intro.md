=! Imports !=

=! Easy !=

==== Easy ====

<<<images/opening_euler.png, height=7cm>>>

=! Thank you !=

==== Problems ====

<<<images/google_import_errorres.png, height=7cm>>>

==== Problems ====

<<<images/medium_import_article.png, height=7cm>>>

==== Problems ====

<<<images/medium_import_article_zoom.png, height=4cm>>>

==== Problems ====

<<<images/stack_ovfl_1.png, height=7cm>>>

==== Problems ====

<<<images/stack_ovfl_2.png, height=7cm>>>

=! Not so easy !=


=! Not so easy !=

<[quote]
In fact it's insane
[quote]>

==== ====

\maketitle

==== About myself ====

* Been using python since 1998
* Contributed to python core
*<2-> !Been driven crazy by import errors!


==== Sources ====

<<<images/sources.png, height=8cm>>>

==== About this talk ====

* Summary of David's tutorial and Erik's book
* David's tutorial is 3 hrs
* Erik's book more 200 pages
* This talk is !15 minutes!
* Applies to Python 3.5 and above
* Intended audience (myself)


==== TL;DR ====

* Mostly works right from Notebook or script
* Gets interesting
** Test environments
** Web apps running from Apache/NGINX/uWSGI
** Serverless Lambda functions
** !Anytime you’ll try to scale up your script!


==== TL;DR : Why ====

* Search path confusion
* Missing or extra \_\_init\_\_ files
* Exotic issues
* !Misunderstanding of the import and module system!

=! Why import ? !=

==== Why import ? ====

* Re-use the code
* From someone else
** Core Developers
<[code][language=Python, numbers=none]
from math import cos
[code]>
** Random people
<[code][language=Python, numbers=none]
import requests
[code]>
* Ourselves
<[code][language=Python, numbers=none]
from x import *
[code]>

=! What import? !=


=! Module !=

==== Module ====

* Used to resolve symbols
* Python type (dict)
* Holds names and references
* Every source file into own module
* Loaded exactly once
* Shared between importers

==== Module ====

script.py
<[code][language=Python]
import a.a as a
import b.b as b
a.set_val(95)
print(b.get_val())
print(a.get_val())
[code]>

a/a.py
<[code][language=Python]
x = 10
def set_val(a): global x ; x = a
def get_val(): return x
def globs(): return globals().keys()
[code]>

b/b.py
<[code][language=Python]
import a.a
def get_val(): return a.a.get_val()
def globs(): return globals().keys()
[code]>


==== Module : Sharing ====

<[columns]

[[[0.6\textwidth]]]

<<<images/import-arrangement.pdf, height=6cm>>>

[[[0.6\textwidth]]]

script.py
<[code][language=Python]
import a.a as a
import b.b as b
a.set_val(95)
print(b.get_val())
print(a.get_val())
[code]>

a/a.py
<[code][language=Python]
x = 10
def set_val(a): global x; x = a
def get_val(): return x
def globs(): return globals().keys()
[code]>

b/b.py
<[code][language=Python]
import a.a
def get_val(): return a.a.get_val()
def globs(): return globals().keys()
[code]>

[columns]>

==== Module ====

<<<images/module_sharing_demo.png, height=6cm>>>

==== Module ====

<<<images/globals_notebook.png, height=8cm>>>



==== Module: Loading ====

* Real dumb
* Read the file
* Make namespace
* Compile
* Return result

==== Module: Loading ====

<[code][language=Python]

def import_module(modname):
    if modname in sys.modules:
        return sys.modules\[modname\]
    source_path = f"share_data/{modname}/{modname}.py"
    with open(source_path, 'r') as f:
        code = f.read()
    mod = types.ModuleType(modname)
    code = compile(code, source_path, 'exec')
    sys.modules\[modname\] = mod
    exec(code, mod.__dict__)
    return sys.modules\[modname\]

import pdb; pdb.set_trace()

[code]>

==== Module: Loading ====

<<<images/module_loading_demo.png, height=6cm>>>


==== Module: Loading ====

<<<images/module_loading_demo.png, height=6cm>>>


==== Module: Loading ====

* Real one is bit more complex
* {Over 3000 lines}(((\url{http://bit.ly/30qJ7T4})))
* Essentially the same
* Real modules have {\_\_init\_\_.py } files

=! Module loaded, now what? !=

==== Module: Import ====

* Import
** Plain
<[code][language=Python, numbers=none]
import x
[code]>
** Relative
<[code][language=Python, numbers=none]
import .y
[code]>
** Select objects
<[code][language=Python, numbers=none]
from math import cos, sin
[code]>
** Everything
<[code][language=Python, numbers=none]
from y import *
[code]>

=! {\_\_init\_\_.py }  !=

==== {\_\_init\_\_.py }  ====

* Annoying
* Make directory into module
* Not really needed in Py3
* But better have them anyway

==== Module: {\_\_init\_\_.py } : what for?  ====

* Mostly empty
* Package code (boto3)(((\url{http://bit.ly/2L7aGuu})))
* Stitch things together
* @export decorator
* Lazy loading

==== Module: {\_\_init\_\_.py } : stitch modules  ====

<[columns]

[[[0.6\textwidth]]]

<<<images/stitching_sub_modules.pdf, height=6cm>>>


[[[0.6\textwidth]]]

{\tiny z/x.py}
<[code][language=Python, basicstyle=\small, numbers=none]
x = 10
def set_val(a):
    global x; x = a
def get_val():
    return x
__all__ = ('set_val',)
[code]>

{\tiny z/y.py}
<[code][language=Python,basicstyle=\small, numbers=none ]
import z.x
def get_val():
    return z.x.get_val()
__all__ = ('get_val',)
[code]>

{\tiny \_\_init.py\_\_}
<[code][language=Python,basicstyle=\small, numbers=none]
from .x import *
from .y import *
__all__ = (y.__all__ + x.__all__)
[code]>

[columns]>

==== Module: {\_\_init\_\_.py } : stitch modules  ====


<<<images/stitching_sub_modules_demo.png, height=6cm>>>

=! What about scripts !=

==== \_\_main\_\_ module ====

* Have no module
* Auto wrapped into module named '\_\_main\_\_'
* Recognize this?
<[code][language=Python, numbers=none]
if __name__ == '__main__':
   your_code_here()
[code]>



==== \_\_main\_\_ module ====

* Ways to run python code
** As script
<[code][numbers=none]
python script.py
[code]>
** As a module (file)
<[code][numbers=none]
python -m script
[code]>

==== \_\_main\_\_ module ====

* Ways to run python code
** As a module (directory)
<[code][numbers=none]
python -m dir
[code]>
** As a zip file
<[code][numbers=none]
python -m zipfile -c hello.zip zip/*.py
python -m file.zip
[code]>

==== \_\_main\_\_ module ====

* More fun with the zip file
<[code]
python -m zipfile -c hello.zip zip/*.py
python hello.zip
[code]>
* Self contained zip

<[code]
python -m zipfile -c hello.zip zip/*.py
python hello.zip
cat zipstub hello.zip > hi
chmod +x hi
./hi
[code]>


==== Real Module Loading ====

* Two step process
* Chain of searchers
* Search to get spec
* Load and link from spec

==== Real Module Loading ====

* Searchers : sys.path searcher
** Most basic
** Goes over the sys path and tries to resolve
** Pays attention to .pth files and such
** Only addresses normal dirs
* Other Searchers
** Look in zips, eggs etc

==== Real Module Loading ====

* Custom searchers
** You can write your own
* Auto install \url{http://bit.ly/2HmNMxO}


=! When things go wrong !=

==== When things go wrong ====

* Remember google search
* Common Problems
** Search path
** Missing init files
** Incorrect directory
** Running as module vs script


==== When things go wrong ====

* See the context
** sys.path
** \_\_spec\_\_

<<<images/tshoot_1.png, height=6cm>>>


==== When things go wrong ====

* python -vvv

<<<images/tshoot_2.png, height=6cm>>>


=! Reloads !=

* Mostly loaded once
* Importing gives loaded module
* Importlib.reload
** Mostly works
** Unless they don't
* See here {\url http://bit.ly/33TDpvc}

=! What next !=

==== What's next ====

* Watch David's Talk
** Make sure to take a break when they take it
* Read Eriks' book

=! ???? !=

=! Thank you !=

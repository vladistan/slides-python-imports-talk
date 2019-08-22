# Export decorator

This is an example of how to implement @export style decorator similar to ES6.

Note that it only affects this style of import statement

```
from x import *
```

When you import your module using the import style shown below, you can access
any symbol inside of x

```
import x
```

![demo](https://github.com/vladistan/slides-python-imports-talk/blob/master/images/exp_dec_tty.gif)

import a.a
import b.b

a.a.set_val(34)

print(b.b.get_val())
print(a.a.get_val())

a.a.set_val(91)

print(b.b.get_val())
print(a.a.get_val())



print ('-' * 15)
print(a.a.globs())


print ('-' * 15)
print(b.b.globs())

import pdb; pdb.set_trace()

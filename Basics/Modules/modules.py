# module = a file containing python code. May contain functions, classes, etc.
#          Used with modular programming, which is to separate a program into parts.

import messages
import messages as m
from messages import hello,bye

m.hello()
messages.bye()
hello()
bye()
# help("modules") # will print all the modules we have access to
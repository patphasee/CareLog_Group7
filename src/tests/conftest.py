# import os
# import sys

# sys.path.append(os.path.abspath('./src/app'))

# python
import os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project root
#print('tests.__init__ imported; ROOT =', ROOT, file=sys.stderr)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
#print('sys.path[0:8] =', sys.path[0:8], file=sys.stderr)
#setup.py
# Backdoor builder
#command line: python setup.py py2exe
from distutils.core import setup 
import py2exe 
setup(
    console=['m09p04.py'],
    #the file you want to compile.
    options = {'py2exe':{'bundle_files':1}}, 
    zipfile = None,
)
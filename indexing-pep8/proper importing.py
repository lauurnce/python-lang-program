# Correct:
import os
import sys

# Wrong:
import sys, os

# Correct:
from subprocess import Popen, PIPE

import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

from . import sibling
from .sibling import example

from myclass import MyClass
from foo.bar.yourclass import YourClass

import myclass
import foo.bar.yourclass
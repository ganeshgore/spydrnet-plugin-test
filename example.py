''' Example user script '''
from posixpath import basename
import sys
import os
sys.path.append(os.getcwd())
from spydrnet.ir import Definition

method_list = [attribute for attribute in dir(Definition) if callable(getattr(Definition, attribute)) and attribute.startswith('__') is False]


print(method_list)
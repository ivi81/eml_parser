'''__init__.py
'''
# -*- coding: utf8 -*-
#!/usr/bin/python3
#import sys
#
import sys
import os
print(os.getcwd())
#sys.path.append('./')
#print(sys.path)
#try:
from .eml_processor import *
from .smtp_stream_handling import *
    #__all__= _smtp_stream_handling.__all__ 
#except Exception: 
 #   from eml_processor import *
  #  from smtp_stream_handling import *

#pprint.pprint(sys.modules) 
#for i in sys.modules:
#    if i.find('.smtp_stream_handling')!=-1 or i.find('smtp_stream_handling')!=-1:
#        print (i)
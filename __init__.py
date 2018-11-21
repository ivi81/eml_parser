# -*- coding: utf8 -*-
#!/usr/bin/python3
import sys
try:
    from ._smtp_processor import *
except Exception:
    sys.path.append('./')
    from _smtp_processor import *
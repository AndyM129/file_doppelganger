#!/usr/bin/env python
# encoding=utf-8

import os
import sys


sys.path.append(f'{os.path.dirname(__file__)}/..')

from kakashi.__init__ import main


if __name__ == '__main__':
    main()


# $ clear; py test.py -f test_proj -t test_proj_2 -m test_proj_map.txt -dv

# $ clear; py test.py -f ../kakashi/kakashi.py -t test_proj_3 -m test_proj_map.txt -dv
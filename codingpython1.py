#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this code is supposed to tell you that the first 10 numbers, which one's
are odd and which one's are even
"""

for counter in range(10):
    if ((counter % 2)==0):
      print(counter)
      print('is even')
    else:
        print(counter)
        print('is odd')
        
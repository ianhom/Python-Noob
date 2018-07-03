#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

d1 = datetime.datetime.now()
d2 = datetime.datetime(2005, 11, 10)
d=(d1-d2).days
print int(d/365)
print int(d/30)
print d
while True:
    pass

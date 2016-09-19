#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks;
print;


localtime = time.localtime(time.time())
print "本地时间为 :", localtime;
print;

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime;
print;

import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;

# result
"""
当前时间戳为: 1474285594.11

本地时间为 : time.struct_time(tm_year=2016, tm_mon=9, tm_mday=19, tm_hour=11, tm_min=46, tm_sec=34, tm_wday=0, tm_yday=263, tm_isdst=0)

本地时间为 : Mon Sep 19 11:46:34 2016

以下输出2016年1月份的日历:
January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""

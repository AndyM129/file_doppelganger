#!/usr/bin/env python
# encoding=utf-8

import os
import time

# =========================================== COPYRIGHT ===========================================
NAME = 'kakashi'
SHORTCUT = 'kks'
DESC = '在保留原文件/目录结构的同时，批量替换指定文本，以快速创建文件分身'
VERSION = '0.1.0'
UPDATE_TIME = '2022/04/08'
AUTHOR_NAME = 'Andy Meng'
AUTHOR_EMAIL = 'andy_m129@163.com'
URL = 'https://github.com/AndyM129/FileDoppelganger'

# =========================================== GLOBAL CONST ===========================================
TIMESTAMP = int(time.time())  # 当前时间戳，eg. 1617351251
DATE_TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(TIMESTAMP))  # 当前时间，eg. 2021-04-02 16:14:11
DATE_STAMP = time.strftime('%Y%m%d%H%M%S', time.localtime(TIMESTAMP))  # 当前时间戳，eg. 20210402161411
FILE = __file__  # 当前文件路径
DIR = os.getcwd()  # 当前的文件目录
BASENAME = os.path.basename(FILE)  # 当前脚本的文件名
BASENAME_WITHOUT_SUFFIX = BASENAME.split('.')[0]  # 文件名（不含后缀）
BASENAME_SUFFIX = BASENAME.split('.')[1]  # 文件后缀

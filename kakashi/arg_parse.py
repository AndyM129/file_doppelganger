#!/usr/bin/env python
# encoding=utf-8

import argparse
from kakashi.consts import *


# 命令行参数解析
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog=NAME,
    prefix_chars='-+',
    description=DESC,
)

# 一级参数
parser.add_argument('-d', '--debug', action='store_true', help='启用调试模式')
parser.add_argument('-v', '--verbose', action='store_true', help='显示详细日志')
parser.add_argument('-V', '--version', action='version', version=VERSION, help='查看当前版本号')
parser.add_argument('-f', '--from_path', help='准备分身的文件或目录的路径')
parser.add_argument('-t', '--to_path', help='文件或目录分身后保存的路径')
parser.add_argument('-m', '--map_path', help='分身时需要替换的内容映射文件路径，每一行为一条映射，每条映射的格式须为"旧文本 => 新文本"')
parser.add_argument('-r', '--remove_if_exist', action='store_true', help='若保存的路径已存在文件，则直接将其删除')

# 解析命令
args = parser.parse_args()

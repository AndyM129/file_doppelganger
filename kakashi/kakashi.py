#!/usr/bin/env python
# encoding=utf-8

from kakashi.logger import *


class Kakashi:

    # 初始化
    def __init__(self):
        print_verbose()
        print_verbose(f'# Kakashi - File Doppelganger')
        print_verbose()

        if args.from_path is None or args.to_path is None:
            parser.print_help()
            parser.exit()

        if not os.path.exists(args.from_path):
            print_fatal(f'原路径不存在：{args.from_path}')

        if os.path.exists(args.to_path):
            if args.remove_if_exist or args.debug:
                os_system(f'rm -rf {args.to_path}')
            else:
                print_fatal(f'保存路径已存在，请先删除，或换个路径：{args.to_path}')

        print_verbose(f'## 解析映射')
        print_verbose()
        self.map = [(args.from_path, args.to_path)]
        if args.map_path is not None and os.path.isfile(args.map_path):
            with open(args.map_path, 'r') as rs:
                lines = rs.read().split('\n')
                for line in lines:
                    line_components = line.split('=>')
                    old = line_components[0].strip()
                    new = line_components[1].strip() if len(line_components) > 0 else ''
                    self.map.append((old, new))
        print_verbose(f'分身时需要替换的内容映射：')
        for old, new in self.map: print_verbose(f'{old} => {new}')
        print_verbose()

        print_verbose(f'## 开始分身')
        print_verbose()
        if os.path.isfile(args.from_path):
            self.doppelganger_file(args.from_path)
        else:
            self.doppelganger_dir(args.from_path)

        print_success()
        print_success(f'## 完成')
        print_success()
        print_success(f'已自动打开保存的目录...')
        os_system(f'open {args.to_path}')
        print_success()


    # 内容替换
    def doppelganger_str(self, from_string):
        to_string = from_string
        for old, new in self.map:
            to_string = to_string.replace(old, new)
        return to_string


    # 分身文件
    def doppelganger_file(self, from_file):
        to_file = self.doppelganger_str(from_file)
        print_success(f'📃 {from_file} ➡️  {to_file}')
        with open(from_file, 'r') as rs:
            content = rs.read()
            content = self.doppelganger_str(content)
            ws = open(to_file, 'w', encoding='utf8')
            ws.write(content)
            ws.close()


    # 分身目录
    def doppelganger_dir(self, from_dir):
        to_dir = self.doppelganger_str(from_dir)
        print_success(f'📂 {from_dir} ➡️  {to_dir}')
        os.makedirs(to_dir) if not os.path.exists(to_dir) else None

        for home, dirs, files in os.walk(from_dir):
            for file in files:
                if file == '.DS_Store': continue
                self.doppelganger_file(f'{home}/{file}')

            for dir in dirs:
                self.doppelganger_dir(f'{home}/{dir}')

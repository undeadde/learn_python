#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import re


# 获取某个目录下所有的文件
def get_all_files(path='.'):
    try:
        if not os.path.isfile(path) and not os.path.isdir(path):
            return []

        if not os.path.isabs(path):
            path = os.path.abspath(path)

        if not os.path.isdir(path):
            return [path]
        else:
            try:
                dirs = os.listdir(path)
                files = []
                for dir in dirs:
                    try:
                        all_files = get_all_files(os.path.join(path, dir))
                        files.extend([os.path.join(file_name) for file_name in all_files])
                    except Exception:
                        continue
            except Exception:
                return []
            return files
    except Exception, err:
        return []


def get_files(path='.', pattern=None):
    ret = []
    all_files = get_all_files(path)
    for file_name in all_files:
        name = os.path.basename(file_name)
        if re.search(pattern, name):
            ret.append(file_name)
    return ret


def count_c_fuction(file_name):
    fn = open(file_name)
    buf = fn.read()
    num = 0
    count = 0
    for character in buf:
        if character == '{':
            num += 1
        elif character == '}':
            num -= 1
            if num == 0:
                count += 1
    fn.close()
    return count


def count_c_file(file_name):
    fn = open(file_name)
    count = 0
    for line in fn.readlines():
        if line == "":
            continue
        else:
            count += 1
    fn.close()
    return count

if __name__ == '__main__':
    files = get_files("..\\..", "\.md$")
    f_count = 0
    line_count = 0
    for f in files:
        f_count += count_c_fuction(f)
        line_count += count_c_file(f)
    print "function num:%s" % f_count
    print "line num:%s" % line_count





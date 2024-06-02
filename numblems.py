#!/usr/bin/python

# https://lazka.github.io/pgi-docs
# pip install pgi
from gi.repository import Gio

import re
import sys
import os

# https://github.com/moses-palmer/pynput
# pip install pynput
from pynput.keyboard import Key, Controller


def main(target_file, act):
    def refresh_window():
        Controller().tap(Key.f5)

    def is_increase(a):
        return a == "inc"

    def increase_num(n):
        if n == 19:
            return -1
        return n + 1

    def decrease_num(n):
        if n == 1:
            return -1
        return n - 1

    def set_one():
        one_emblem = "emblem-num-" + str(1) + "-symbolic"
        emblems.append(one_emblem)
        set_emblems(emblems)

    def set_emblems(embs):
        testfile_info.set_attribute_stringv("metadata::emblems", embs)
        testfile.set_attributes_from_info(testfile_info, 0)
        refresh_window()

    num_emblem_regex = re.compile("^emblem-num-[0-9]+-symbolic$")
    testfile = Gio.file_new_for_path(target_file)
    testfile_info = testfile.query_info('metadata::emblems', 0)
    emblems = testfile_info.get_attribute_stringv("metadata::emblems")
    num_emblem_found = False
    '''if testfile_info is None:'''
    if len(emblems) == 0:
        print("No emblems, set one if needed (on increase command)")
        #exit()
    else:
        for i in range(0, len(emblems)):
            if num_emblem_regex.match(emblems[i]):
                num_emblem_found = True
                num = int(emblems[i].split("-")[2])

                if is_increase(act):
                    num = increase_num(num)
                else:
                    num = decrease_num(num)

                if num == -1:
                    emblems.pop(i)
                    set_emblems(emblems)
                    exit()
                else:
                    new_num_emblem = "emblem-num-" + str(num) + "-symbolic"
                    emblems[i] = new_num_emblem
                    set_emblems(emblems)
                    exit()

    if not num_emblem_found:
        # print("No num emblem, set 1")
        if is_increase(act):
            set_one()

        exit()


def show_help():
    print("Usage:")
    print("Increase: num_emblem <filepath> <inc>")
    print("Decrease: num_emblem <filepath> <dec>")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[2] not in ["inc", "dec"]:
        show_help()
    else:
        if os.path.exists(sys.argv[1]):
            main(sys.argv[1], sys.argv[2])

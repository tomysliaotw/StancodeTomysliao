"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    s = False
    for i in name_data:
        if i == name:
            s = True
    if s:
        if year not in name_data[name]:
            name_data[name][year] = rank
        elif int(name_data[name][year]) > int(rank):
            name_data[name][year] = rank
    else:
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    with open(filename, 'r') as f:
        year = filename[5:8]
        i = 0
        for line in f:
            line = line.strip()
            if i == 0:
                year = line
                i = 1
            else:
                rank, boy, girl = line.split(',')
                rank = rank.strip()
                boy = boy.strip()
                girl = girl.strip()
                add_data_for_name(name_data, year, rank, boy)
                add_data_for_name(name_data, year, rank, girl)


def read_files(filenames):
    name_data = {}
    for i in filenames:
        add_file(name_data, i)
    return name_data


def search_names(name_data, target):
    ret = []
    target = target.lower()
    for i in name_data:
        b = i.lower()
        if target in b:
            ret.append(i)
    return ret


def print_names(name_data):
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)
    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

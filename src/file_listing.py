#!/usr/bin/env python3

from calendar import day_abbr
from ctypes import sizeof
import re


def file_listing(filename="src/listing.txt"):
    line_list = []
    with open(filename, "r") as f:
        for line in f:
            mo = re.search(r'(\d+)\s([A-Za-z]{3})\s*(\d{1,2})\s(\d{2}):(\d{2})\s(.*)', line)
            #print(list(mo))
            if mo:
                list_of_data = mo.groups()
                size = int(mo.group(1))
                month = mo.group(2)
                day = int(mo.group(3))
                hour = int(mo.group(4))
                minute = int(mo.group(5))
                file_name = mo.group(6)
                
                line_list.append((size,month,day,hour,minute,file_name))
            
    return line_list

def main():
    file_listing()

if __name__ == "__main__":
    main()

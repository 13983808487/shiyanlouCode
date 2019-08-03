#!/usr/bin/env python3
import sys

def copy_file(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            for index,value in enumerate(src_file.readlines()):#之前写的src.readlines......错了两处
                dst_file.write('{} {}'.format(index+1,value))


if __name__ == "__main__":
    if len(sys.argv)==3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print("Parameter Error")
        print(sys.argv[0],"srcfile dstfile")
        sys.exit(-1)
    sys.exit(0)

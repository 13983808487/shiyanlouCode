#!/usr/bin/env python3

import sys
dic={}

def handle_data(arg):
    k,v=arg.split(':')
    dic[k]=v

if __name__=='__main__':
    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in dic:
        print('ID:'+key,'Name:'+dic[key])

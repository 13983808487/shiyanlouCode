#!/usr/bin/env python3

import sys
a=sys.argv[1]
a=int(a)
if a >=0 and a<10:
        print('you belong to kids')
elif a>=10 and a<18:
        print('you belong to teenager')
elif a>=18 and a<30:
        print('you belone to adult')
elif a>=30 and a<60:
        print('you belone to older')
elif a>=60 and a<120:
        print('you belong to oldest')

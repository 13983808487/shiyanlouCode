#!/usr/bin/env python3

import sys


if len(sys.argv)!=2:
    print("Parameter Error")
    sys.exit()
try:
    wage=int(sys.argv[1])
except:
    print("Parameter Error")
#taxable_income
ti=wage-5000
if ti<=0:
    print(format(0,".2f"))
elif ti<=3000:
    t=ti*0.03-0
    print(format(t,".2f"))
elif ti>3000 and ti<=12000:
    t=ti*0.1-210
    print(format(t,".2f"))
elif ti>12000 and ti<=25000:
    t=ti*0.2-1410
    print(format(t,".2f"))
elif ti>25000 and ti<=35000:
    t=ti*0.25-2660
    print(format(t,".2f"))
elif ti>35000 and ti<=55000:
    t=ti*0.3-4410
    print(format(t,".2f"))
elif ti>55000 and ti <=80000:
    t=ti*0.35-7160
    print(format(t,".2f"))
else:
    t=ti*0.45-15160
    print(format(t,".2f"))

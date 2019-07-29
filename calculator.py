#!/usr/bin/env python3

import sys

def income(key,wage):
    #taxable_income
    ti=wage*(1-0.165)-5000
    if ti<=0:
        t=0
    elif ti<=3000:
        t=ti*0.03-0
    elif ti>3000 and ti<=12000:
        t=ti*0.1-210
    elif ti>12000 and ti<=25000:
        t=ti*0.2-1410
    elif ti>25000 and ti<=35000:
        t=ti*0.25-2660
    elif ti>35000 and ti<=55000:
        t=ti*0.3-4410
    elif ti>55000 and ti <=80000:
        t=ti*0.35-7160
    else:
        t=ti*0.45-15160
    later_wage=wage-t-wage*0.165
    print(key+":"+format(later_wage,".2f"))

income_dict={}

for i in sys.argv[1:]:
    str_=i.split(':')
    try:
        wage=int(str_[1])
    except:
        print("Parameter Error")
    income_dict[str_[0]]=wage
for key,value in income_dict.items():
    income(key,value)



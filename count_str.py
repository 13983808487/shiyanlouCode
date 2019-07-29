#!/usr/bin/env python3

def char_count(str_):
    char_dict={}
    for char in str_:
        c=char_dict.get(char)
        if c is None:
            char_dict[char]=1
        else:
            char_dict[char]+=1
    for key,value in char_dict.items():
        print(key,value)
if __name__ == '__main__':
    c=input("Enter a string: ")
    char_count(c)

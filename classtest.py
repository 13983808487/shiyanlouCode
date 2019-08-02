#!/usr/bin/env python3
class UserData(object):
    def __init__(self,id,name):
        self.id=id
        self._name=name


class NewUser(UserData):
    group='shiyanlou-louplus'

    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id,name):
        return '{1}\'s id is {0}'.format(id,name)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    def __call__(self):
        print('{}\'s id is {}'.format(self._name,self.id))

if __name__=='__main__':
    user=NewUser(101,'Jack')
    user()

# -*- coding:utf-8 -*-
# http://www.cnblogs.com/Eva-J/articles/7293890.htm

def person(name, age, sex, job):
    def walk(p):
        print("person %s is walking..." % p['name'])

    data = {
        'name': name,
        'age': age,
        'sex': sex,
        'job': job,
        'walk': walk
    }

    return data


def dog(name, dog_type):
    def bark(d):
        print("dog %s:wang.wang..wang..." % d['name'])

    data = {
        'name': name,
        'type': dog_type,
        'bark': bark
    }

    return data

d1 = dog("wangcai","hashiqi")
p1 = person("james",36,"F","Doctor")
p2 = person("harden",27,"F","Teacher")

d1['bark'](p1)



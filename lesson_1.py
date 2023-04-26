#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def add(a,b):
    #先尝试下浮点化,用作判断是否为整数或者数字
    try:
        x = float(a)
        y = float(b)
        #判断超范围与否
        if abs(x) > 99.0 or abs(y) > 99.0:
            print(f'输入的数字范围超过99或者小于-99')
            return
        else:
            print(f'{a}+{b}={x + y}')
            return (x + y)
    except ValueError:
        print('输入的不是数字！')
if __name__ == '__main__':
    #判断输入 一般就是参数传多传少,格式对的话进入函数自己判断传的类型
    try:
        x,y=(input('请输入要相加的两个数,用空格隔开:').split(' '))
        add(x,y)
    except ValueError:
        print('传参不对,需要输入两个哦')
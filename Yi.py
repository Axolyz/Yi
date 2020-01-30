# -*- coding: utf-8 -*-
# @Author: Li Baoyan
# @Date:   2019-07-18 11:52:00
# @Last Modified by:   Administrator
# @Last Modified time: 2019-07-22 12:12:24


import random


def rem_minus(x):
    xrem = x % 4
    if xrem == 0:
        xrem = 4
    else:
        pass
    x = x - xrem
    return x


switch = ''
while switch != 'q':
    input('举意完毕后按回车继续。')
    bos = []
    for c in range(6):
        n = 50
        n = n - 1
        for o in range(3):
            x = random.randint(1, n - 1)
            y = n - x
            p = random.randint(0, 1)
            if p == 0:
                x = x - 1
            elif p == 1:
                y = y - 1
            x = rem_minus(x)
            y = rem_minus(y)
            n = x + y
        bo = int(n / 4)
        bos.insert(0, bo)
    print("本卦：")
    for bo in bos:
        if bo == 6 or bo == 8:
            print("---   ---")
        elif bo == 7 or bo == 9:
            print('---------')
    print("之卦：")
    for bo in bos:
        if bo == 9 or bo == 8:
            print("---   ---")
        elif bo == 7 or bo == 6:
            print('---------')
    switch = input('请查看程序所在目录下的卦名对照表自行解卦。\n输入q退出，输入任意值重来。')

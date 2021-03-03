#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
# (C) 2000-2021 NSFOCUS Corporation. All rights Reserved#
#########################################################
import cherry
import time


def train(model, lang):
    cherry.train(model, lang)


def check(model, lang):
    pfm = cherry.performance(model, lang)
    pfm.get_score()


if __name__ == '__main__':
    # 样本集目录名称
    model = r'E:\xiangrisheng\xrs\py\机器学习\datasets\sensitive6'
    lang = 'Chinese'
    time1 = time.time()
    train(model, lang)
    # check(model, lang)
    time2 = time.time()
    print('spend {0}s'.format(time2-time1))

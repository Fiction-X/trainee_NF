#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
# (C) 2000-2021 NSFOCUS Corporation. All rights Reserved#
#########################################################
# 对测试样本进行预测和判别
import cherry
import os
import time
import shutil
from multiprocessing import Process


def test_samples(sample_path, category, model):
    def rm(st, sample_path, filename):
        if st == 1:
            os.remove(sample_path + '/' + filename)

    print(model, sample_path, category)
    filenames = [d for d in sorted(os.listdir(sample_path))]
    total = len(filenames)
    textlist = []
    positive = 0
    negtive = 0
    invalid = 0
    st = 0
    start = time.time()
    for filename in filenames:
        try:
            if filename.endswith('txt'):
                with open(os.path.join(sample_path, filename),
                          'r',
                          encoding='utf-8') as f:
                    text = f.read()
                    if text:
                        st = 0
                        res = cherry.classify(model, text=text)
                        pbt = res.get_probability()[0]
                        res.get_word_list()
                        if pbt[category] > pbt[abs(1 - category)]:
                            positive += 1
                        else:
                            st = 1
                            negtive += 1
                            textlist.append(filename)
                            # 复制问题样本
                            shutil.copy(
                                (sample_path + '/' + filename),
                                "C:/Users/nsfocus/Desktop/ques")
                    else:
                        invalid += 1
                        # print('invalid:' + filename)
        except (Exception):
            import traceback
            print(traceback.format_exc())
        # 删除检查目录的问题样本
        rm(st, sample_path, filename)

    result = positive, negtive, invalid, total
    print('%s used %ds' % (sample_path, time.time() - start), result)
    time.sleep(1)
    if textlist == []:
        pass
    else:
        print(textlist)


def test(model, paths):
    ps = []
    for root in paths:
        folders = [
            os.path.join(root, folder) for folder in sorted(os.listdir(root))
        ]
        for folder in folders:
            category = 0 if folder.find('abnormal') > -1 else 1
            p = Process(target=test_samples, args=(folder, category, model))
            p.start()
            ps.append(p)
    for p in ps:
        p.join()


def test2():
    model = 'sensitive6'
    paths = ['datasets/sensitive3_validation']
    test(model, paths)


def test3():
    model = 'sensitive6'
    paths = ['datasets/sensitive2_validation']
    test(model, paths)


def test4():
    model = 'sensitive6'
    paths = ['datasets/sensitive2']
    test(model, paths)


def test5():
    model = 'sensitive6'
    paths = ['datasets/sensitive6']
    test(model, paths)


if __name__ == '__main__':
    # test2()
    # test3()
    test4()
    # test5()

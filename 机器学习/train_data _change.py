import cherry
import os
import re
import time
import redis
from multiprocessing import Pool

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

r.set("positive", 0)
r.set("negtive", 0)
r.set("invalid", 0)


def test_samples(start, folder, sample_path, category, model):
    try:
        if sample_path.endswith('txt'):
            with open(sample_path, 'r', encoding='utf-8') as f:
                text = f.read()
                if text:
                    res = cherry.classify(model, text=text)
                    pbt = res.get_probability()[0]
                    res.get_word_list()
                    if pbt[category] > pbt[abs(1 - category)]:
                        num = int(r.get("positive")) + 1
                        r.set("positive", num)
                        time.sleep(0.5)
                    else:
                        num = int(r.get("negtive")) + 1
                        txtname = re.findall(r"[0-9]+\.[a-z]+", sample_path)
                        print(''.join(txtname))
                        r.set("negtive", num)
                        time.sleep(0.5)
                else:
                    num = int(r.get("invalid")) + 1
                    r.set("invalid", num)
                    txtname = re.findall(r"[0-9]+\.[a-z]+", sample_path)
                    print('无效:' + ''.join(txtname))
                    time.sleep(0.5)

        else:
            paths = os.listdir(sample_path)
            for path in paths:
                if path.endswith('txt'):
                    with open(sample_path + '/' + path, 'r',
                              encoding='utf-8') as f:
                        text = f.read()
                    if text:
                        res = cherry.classify(model, text=text)
                        pbt = res.get_probability()[0]
                        res.get_word_list()
                        if pbt[category] > pbt[abs(1 - category)]:
                            num = int(r.get("positive")) + 1
                            r.set("positive", num)
                            time.sleep(0.5)
                        else:
                            num = int(r.get("negtive")) + 1
                            txtname = re.findall(r"[0-9]+\.[a-z]+", path)
                            print(''.join(txtname))
                            r.set("negtive", num)
                            time.sleep(0.5)
                    else:
                        num = int(r.get("invalid")) + 1
                        r.set("invalid", num)
                        txtname = re.findall(r"[0-9]+\.[a-z]+", path)
                        print('无效:' + ''.join(txtname))
                        time.sleep(0.5)
    except (Exception):
        import traceback
        try:
            print(sample_path + '出错!')
        except(Exception):
            print(path + '出错!')
        print(traceback.format_exc())


def test(model, folder):
    r.flushdb()
    pool = Pool(processes=10)
    start = time.time()
    print("folder:" + folder)
    category = 0 if folder.find('abnormal') > -1 else 1
    for file in os.listdir(folder):
        file = folder + "\\" + file
        # print("file:" + file)
        pool.apply_async(test_samples, (start, folder, file, category, model))
    pool.close()
    pool.join()
    print("%.2f" % (time.time() - start))
    print(len(os.listdir(folder)))
    print(r.get("positive"))
    print(r.get("negtive"))
    print(r.get("invalid"))


def test1():
    model = 'sensitive4'
    folder = 'datasets/sensitive3/normal'
    test(model, folder)


def test2():
    model = 'sensitive6'
    folder = 'datasets/sensitive3/normal'
    test(model, folder)


def test3():
    model = 'sensitive4'
    folder = 'datasets/sensitive3/abnormal'
    test(model, folder)


def test4():
    model = 'sensitive6'
    folder = 'datasets/sensitive3/abnormal'
    test(model, folder)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()

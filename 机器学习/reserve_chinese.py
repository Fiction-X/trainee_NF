import os
import re
import time


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            if file_path.endswith('.txt'):
                list_name.append(file_path)
                alter(file_path)
            else:
                pass
    return (list_name)


def alter(file_path):
    data = ''
    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.read()
        data = re.sub('[^\u4E00-\u9FA5]', "", data)
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    list_name = []
    start_time = time.time()
    path = 'data_html/abnormal'
    # pool = Pool(processes=10)
    # pool.apply_async(listdir, (path, list_name))
    # pool.close()
    # pool.join()
    listdir(path, list_name)
    res = listdir(path, list_name)
    print(len(res))
    print('spend {0}s'.format(time.time() - start_time))

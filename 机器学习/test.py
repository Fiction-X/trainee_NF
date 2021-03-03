import cherry

res = cherry.performance('sensitive3')

res = cherry.classify('sensitive3', text="Hello World Nsfocus")
print(res.get_word_list())
# import filecmp
# # true if 2 files are the same
# result = filecmp.cmp(file1, file2)
# str = ['101460283.html.txt', '103342915.html.txt', '103401647.html.txt', '103430325.html.txt', '105545771.html.txt', '109200520.html.txt', '109238994.html.txt', '109449261.html.txt', '109593667.html.txt', '109949069.html.txt', '109968045.html.txt', '109978403.html.txt', '110045597.html.txt', '110085757.html.txt', '110098097.html.txt', '110103819.html.txt', '110107173.html.txt', '110214051.html.txt', '110285925.html.txt', '110292333.html.txt', '110293369.html.txt', '110299871.html.txt', '110314225.html.txt', '110314467.html.txt', '110341147.html.txt', '110377139.html.txt', '110447597.html.txt', '110457837.html.txt', '110462611.html.txt', '110472049.html.txt', '110484059.html.txt', '110715967.html.txt', '110716019.html.txt', '110729935.html.txt', '110737273.html.txt', '110744829.html.txt', '110746109.html.txt', '110753589.html.txt', '110804515.html.txt', '110805251.html.txt', '110845999.html.txt', '110885467.html.txt', '110941381.html.txt', '110950621.html.txt', '110968011.html.txt', '110976709.html.txt', '111034723.html.txt', '111064199.html.txt', '111135275.html.txt', '111470607.html.txt', '111761759.html.txt', '111788351.html.txt', '112326507.html.txt', '112449719.html.txt', '112667099.html.txt', '112696665.html.txt', '112721429.html.txt', '112725455.html.txt', '112729597.html.txt', '112758563.html.txt', '112807669.html.txt', '112851633.html.txt', '112863349.html.txt', '112909253.html.txt', '112911623.html.txt', '112921209.html.txt', '112951613.html.txt', '112951869.html.txt', '112959069.html.txt', '113016231.html.txt', '113016267.html.txt', '113056513.html.txt', '113063351.html.txt', '113075091.html.txt', '113108797.html.txt', '113109611.html.txt', '113178941.html.txt', '113198267.html.txt', '113206617.html.txt', '113212395.html.txt', '113230391.html.txt', '113232003.html.txt', '113265457.html.txt', '113297813.html.txt', '113338509.html.txt', '113363095.html.txt', '113424413.html.txt', '113446135.html.txt', '113461091.html.txt', '113469625.html.txt', '113510111.html.txt', '113511603.html.txt', '113514869.html.txt', '113515291.html.txt', '113525003.html.txt', '113721873.html.txt', '113779081.html.txt', '114137719.html.txt', '114260793.html.txt', '114260827.html.txt', '114260829.html.txt', '114273955.html.txt', '114356305.html.txt', '114620897.html.txt', '114621147.html.txt', '115050823.html.txt', '115889119.html.txt', '116183975.html.txt', '116196087.html.txt', '116720429.html.txt', '117001613.html.txt', '117002637.html.txt', '117002641.html.txt', '117002691.html.txt', '117006487.html.txt', '117056333.html.txt', '117057147.html.txt', '117329965.html.txt', '117333471.html.txt', '117337007.html.txt']
# for i in str:
#     print(i)

# import re
# str = r'datasets/sensitive2_validation/normal_validation\118343545.html.txt'
# abc = re.findall(r"[0-9]+\.[a-z]+", str)
# print(abc)

# # 将txt中的文件名 移动出来
# import os
# import shutil
# arr = []
# path = 'samples2'
# for line in open('move_need.txt', 'r', encoding='utf-8'):
#     arr.append(line.replace('\n', ''))
# if os.path.isdir(path) is True:
#     files = os.listdir(path)
#     for file in files:
#         for i in arr:
#             st = os.path.isfile(os.getcwd() + '/' + path + '/' + file + '/' +
#                                 i)
#             if st is True:
#                 shutil.copy(os.getcwd() + '/' + path + '/' + file + '/' + i,
#                             "E:\\xiangrisheng\\xrs\\py\\机器学习\\datasets")

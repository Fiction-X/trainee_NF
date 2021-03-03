# import filecmp
# # true if 2 files are the same
# result = filecmp.cmp(file1, file2)
# str = [
#     '118294439.html.txt', '118294483.html.txt', '118297083.html.txt',
#     '118297367.html.txt', '118297473.html.txt', '118299529.html.txt',
#     '118299531.html.txt', '118299551.html.txt', '118299557.html.txt',
#     '118299561.html.txt', '118314487.html.txt', '118317505.html.txt',
#     '118317511.html.txt', '118319345.html.txt', '118319349.html.txt',
#     '118326719.html.txt', '118326721.html.txt', '118326739.html.txt',
#     '118335175.html.txt', '118335221.html.txt', '118335295.html.txt',
#     '118335387.html.txt', '118337565.html.txt', '118338063.html.txt',
#     '118338065.html.txt', '118338149.html.txt', '118339343.html.txt',
#     '118339407.html.txt', '118339411.html.txt', '118339817.html.txt',
#     '118341955.html.txt', '118341957.html.txt', '118343541.html.txt',
#     '118343545.html.txt', '118343553.html.txt', '118343575.html.txt',
#     '118344097.html.txt', '118345663.html.txt', '118345671.html.txt',
#     '118345731.html.txt', '118346163.html.txt', '118346165.html.txt',
#     '118346403.html.txt', '118349181.html.txt', '118350717.html.txt',
#     '118350719.html.txt', '118350731.html.txt', '118350853.html.txt',
#     '118350875.html.txt', '118350973.html.txt', '118354413.html.txt',
#     '118354495.html.txt', '118355481.html.txt', '118355515.html.txt',
#     '118355517.html.txt', '118355877.html.txt', '118356047.html.txt',
#     '118356105.html.txt', '118356107.html.txt', '118356133.html.txt',
#     '118358221.html.txt', '118358229.html.txt', '118358417.html.txt',
#     '118358443.html.txt', '118359139.html.txt', '118359447.html.txt',
#     '118359509.html.txt', '118359511.html.txt', '118360013.html.txt',
#     '118360195.html.txt', '118360235.html.txt', '118360237.html.txt',
#     '118360265.html.txt', '118360305.html.txt', '118361143.html.txt',
#     '118361179.html.txt', '118361181.html.txt', '118361183.html.txt',
#     '118361185.html.txt', '118361187.html.txt', '118361191.html.txt',
#     '118361195.html.txt', '118361277.html.txt', '118361645.html.txt',
#     '118362267.html.txt', '118362745.html.txt', '118362755.html.txt',
#     '118362849.html.txt', '118362857.html.txt', '118362871.html.txt'
# ]
# for i in str:
#     print(i)
# url = 'http://www.cib.com.cn/cn/index.html'
# # if 'https' in url:
# #     print(url)
# name = '19990306'
# for i in range(10, 20):
#     with open((name+str(i)+'.txt'), 'w', encoding='utf-8') as f:
#         f.write('')
for i in range(1, 4):
    with open(str(i)+'.txt', 'r', encoding='utf-8') as f:
        a = f.read()
        a = a.replace('\n', '')
    open(str(i)+'.txt', 'w', encoding='utf-8').write('')
    with open(str(i)+'.txt', 'w+', encoding='utf-8') as f:
        f.write(a)

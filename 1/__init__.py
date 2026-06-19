import os, ast
from set import *


AppsDict = {'设置':'设置'}
if not os.path.exists('.\__apps.path'):
    with open('.\__apps.path','a+',encoding='UTF-8') as f:
        print(AppsDict,file=f,end='')
        print('__apps.path was created successfully!')
if not os.path.exists('.\__local_drives.path'):
    str1 = '%s \t %s'
    str2 = ('序号', '盘符')
    print(str1%str2)
    str1 = '%02d. \t|\t %s'
    drives_dict = get_drives()
    for x, y in drives_dict.items():
        str2 = (x, y)
        print(str1 % str2)
    x += 1
    str2 = (x, '完成')
    print(str1 % str2)
    local_drives = []
    while True:
        try:
            num = int(input('请输入本地盘符的序号(exit退出)：'))
            if num == x:
                break
            choice = drives_dict[num]
        except:
            exit('error:incorrect input(choose number)!')
        local_drives.append(choice)

    with open('.\__local_drives.path', 'a+', encoding='UTF-8') as f:
        print(local_drives, file=f, end='')
        print('__local_drives.path was created successfully!')


while True:

    with open('.\__apps.path', 'r', encoding='UTF-8') as f:
        print('__apps.path was found!')
        AppsDict = ast.literal_eval(f.read())

    NumDict = {}
    str1 = '%s \t %s'
    str2 = ('序号', '应用/操作')
    print(str1 % str2)
    str1 = '%02d. \t|\t %s'
    num = 0
    for x, _ in AppsDict.items():
        num += 1
        NumDict[num] = x
        str2 = (num, x)
        print(str1 % str2)
    num += 1
    NumDict[num] = '退出'
    str2 = (num, '退出')
    print(str1 % str2)

    try:
        num = int(input('请输入应用/操作相应的序号：'))
        choice = NumDict[num]
    except:
        exit('error:incorrect input(choose number)!')
    if choice == '设置':
        print('您选择了：设置')
        from menu import menu
        menu()
    elif choice == '退出':
        print('正在退出...')
        break
    else:
        print(f'您选择了：{choice}')
        break




'''

F:\Entity-122425111303\Python编程\apps_launcher\__path.txt
F:\Entity-122425111303\软件\path
输入本地盘符并保存    启动应用
开发U盘专属版，判断U盘盘符，运行应用
用弹窗代替print

'''
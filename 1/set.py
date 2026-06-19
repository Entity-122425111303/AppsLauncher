

def insert_app():
    from choose import choose
    import ast
    while True:
        with open('.\__apps.path', 'r', encoding='UTF-8') as f:
            AppsDict = ast.literal_eval(f.read())
        with open('.\__local_drives.path', 'r', encoding='UTF-8') as f:
            local_drives = f.read()
        print('返回请输入exit')
        AppName = input('请输入应用名：')
        if AppName == 'exit':
            break
        for x,y in AppsDict.items():
            if AppName == x:
                judge = input('是否替换原应用？(y/n)')
                if judge == 'n':
                    judge = input('是否更改应用名？(y/n)')
                    if judge == 'n':
                        print('正在退出...')
                        exit(0)
                    elif judge == 'y':
                        AppName = input('请输入新的应用名：')
                    else:
                        exit('incorrect input(judge error2)!')
                elif judge == 'y':
                    break
                else:
                    exit('incorrect input(judge error1)!')
            else:
                break
        print('请在窗口中选择文件，退出请取消')
        catch = choose()
        p = catch.choose_file()
        if p is None:
            break
        if p[0] not in local_drives:
            AppPath = p.split('/', 1)[-1]
        else:
            AppPath = p
        print(AppPath)
        AppsDict[AppName] = AppPath
        with open('.\__apps.path', 'w', encoding='UTF-8') as f:
            print(AppsDict, file=f, end='')
            print('successfully')


def get_drives() -> dict[int, str]:
    import ctypes
    import string
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    drives = []
    for letter in string.ascii_uppercase:
        if drive_bitmask & 1:
            drives.append(letter)
        drive_bitmask >>= 1
    n = 0
    drives_dict = {}
    for x in drives:
        n += 1
        drives_dict[n] = x
    return drives_dict


def delete_app():
    import ast
    with open('.\__apps.path', 'r', encoding='UTF-8') as f:
        AppsDict = ast.literal_eval(f.read())
    print('请选择想删除的应用')
    n = 0
    dict1 = {}
    str1 = '%s \t %s'
    str2 = ('序号', '应用/操作')
    print(str1 % str2)
    str1 = '%02d. \t|\t %s'
    for x,y in AppsDict.items():
        if x == '操作菜单':
            continue
        n += 1
        str2 = (n,x)
        print(str1 % str2)
        dict1[n] = x
    n += 1
    print(str1 % (n,'返回'))
    dict1[n] = x
    try:
        choice = dict1[int(input('输入序号:'))]
    except:
        print('error:incorrect choice')
        return False
    if choice == '返回':
        return True


if __name__ == '__main__':
    insert_app()


'''
    F:\Entity-122425111303\Python编程\apps_launcher\__path.txt
    F:\Entity-122425111303\软件\path
    删除  重命名   若本地盘符，直接写入，其他去掉盘符，正则表达式判断，写入
'''


def insert_app(AppName, AppPath, FilePath):
    '''使用前请检查path文件夹、__path.txt是否创建
        请确保AppName是否与现有重复
        AppPath:  e.g.Entity-122425111303\\apps\...
                        e.g.Entity-122425111303\\软件\...'''

'''
    print('请确保Entity-122425111303文件夹的根目录为盘符')
    import os,re
    if not os.path.exists(FilePath):
        exit('error:cannot find file(FilePath error)!')
    Apps1 = os.listdir(FilePath)
    Apps2 = []
    for x in Apps1:
        y = x.split('.')
        if 'txt' in y:
            y.remove('txt')
        a = '.'.join(y)
        Apps2.append(a)
#    print(Apps2)
    while True:
        if AppName in Apps2:
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
    TxtPath = FilePath + '\\' + AppName + '.txt'
#    print(TxtPath)
    if re.match('^Entity-122425111303/(apps|软件)/(.*/*)*\w+\.(bat|exe)$', AppPath) is None:
        print('incorrect AppPath')
        return False
    else:
        with open(TxtPath, 'w+') as f:
            print(AppPath, file=f, end='')
        print('success')
        return True

def delete_app(FilePath):
    while True:
        import os
        Apps = os.listdir(FilePath)
        z = 1
        AppsName_dict = {1:'返回'}
        AppsFullName_dict = {1:'返回'}
        for x in Apps:
            y = x.split('.')
            if 'txt' in y:
                y.remove('txt')
            a = '.'.join(y)
    #        print(a)
            z += 1
            AppsName_dict[z] = a
            AppsFullName_dict[z] = x

#        print(AppsFullName_dict)


        str1 = '%s \t %s'
        str2 = ('序号', '应用/操作')
        print(str1 % str2)
        str1 = '%02d. \t|\t %s'
        for key, AppName in AppsName_dict.items():
            str2 = (key, str(AppName))
            print(str1 % str2)

        try:
            num = int(input('请输入应用/操作相应的序号：'))
            AppsFullName_dict[num]
        except:
            exit('error:incorrect input(choose number)!')

        if num == 1:
            return True
        else:
            TxtPath = FilePath+'\\'+AppsFullName_dict[num]
            os.remove(TxtPath)
            print('successfully')


if __name__ == '__main__':
    if not delete_app(r'F:\Entity-122425111303\软件\path'):
        print('error')


'''
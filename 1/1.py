

'''

#    print(AppsFullName_dict)

    str1 = '%s \t %s'
    str2 = ('序号', '应用/操作')
    print(str1%str2)
    str1 = '%02d. \t|\t %s'
    str2 = (1, '操作菜单')
    print(str1%str2)


    try:
        num = int(input('请输入应用/操作相应的序号：'))
    except:
        exit('error:incorrect input(choose number)!')
    if num == 1:
        print('您选择了：打开操作菜单')
        from menu import menu
        menu(FilePath)
    elif num == 2:
        print('正在退出...')
        exit(0)
    else:
        try:
            AppsName_dict[num]
        except:
            exit('error:incorrect number(choose number)!')
        NameFilePath = FilePath+'\\'+AppsFullName_dict[num]
        with open(NameFilePath,'r') as f:
            AppPath = f.read()
#            print(AppPath)
        if AppsName_dict[num] == 'piper':
            p = 'F'
        else:
            p = str(input(f'请输入 {AppsName_dict[num]} 所在盘符(仅字母)：'))
#        print(p)
        AppPath1 = p+':\\'+AppPath
        if not os.path.exists(AppPath1):
            exit('incorrect AppPath(open app)!')
        print('正在打开：', AppsName_dict[num])
        os.startfile(AppPath1)
'''
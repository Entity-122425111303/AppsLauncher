



def menu():
    while True:
        menu1 = {1:'增加', 2:'删除', 3:'重命名', 4:'返回'}
        str1 = '%s \t %s'
        str2 = ('序号', '操作')
        print(str1 % str2)
        str1 = '%02d. \t|\t %s'
        for key, Name in menu1.items():
            str2 = (key, str(Name))
            print(str1 % str2)

        try:
            num = int(input('请输入操作相应的序号：'))
            choice = menu1[num]
        except:
            exit('error:incorrect input(choose number)!')


        if choice == '返回':
            break
        elif choice == '增加':
            from set import insert_app
            insert_app()
        elif menu1[num] == '删除':
            from set import delete_app
            while True:
                if delete_app():
                    break


if __name__ == '__main__':
    menu()

#F:\Entity-122425111303\软件\path
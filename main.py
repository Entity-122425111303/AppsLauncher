import json, sys, QT_PLUGIN_PATH_INSERT, pyuac, argparse
from uiclses import *
from operatefuncs import *

parser = argparse.ArgumentParser(description='AppsLauncher.exe')
parser.add_argument('-a',
                    '-AppName',
                    help='AppName',
                    type=str,
                    nargs='*',
                    action='store',
                    default=False,
                    dest='AppName',
                    )
parser.add_argument('-t', '-test', help='TestMode', default=False, action='store_true', dest='test')
args = parser.parse_args()

mode = {'test': args.test, 'LinkStart': args.AppName}

false, ture, null = False, True, None
app = QtWidgets.QApplication(sys.argv)
__AppPath = {'exit': AppDir('AppsLauncher', 'exit', ExitCode=0)}
NewApp: tuple = ()

# 从各个盘的根目录下读取AppName,AppPath
AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), mode)

if mode['LinkStart']:
    try:
        path_switch(AppDir('AppsLauncher', 'app', operate='open', Name=mode['LinkStart']['Name']), mode)
    except:
        print('error\r\n打开主程序')
    else:
        exit()


# 主程序
def main():
    if not os.path.exists('./data'):
        os.mkdir('./data')
    if not os.path.exists('./data/settings.json'):
        with open('./data/settings.json', 'w', encoding='utf8') as f:
            settings = {'确认删除': True, '打开不关闭': False}
            json.dump(settings, f, ensure_ascii=False, indent=4)
    else:
        with open('./data/settings.json', 'r', encoding='utf8') as f:
            if not f.read():
                with open('./data/settings.json', 'w', encoding='utf8') as f:
                    settings = {'确认删除': True, '打开不关闭': False}
                    json.dump(settings, f, ensure_ascii=False, indent=4)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, mode)

    if mode['test']:
        ui.add_choice_to_viewlist({'app1': 1, 'app2': 2, 'app3': 3})  # type:ignore # 测试用

    ui.add_choice_to_viewlist(path_switch(AppDir('AppsLauncher', 'app', operate='get'), mode))

    MainWindow.show()
    ExitCode = app.exec_()
    path_switch(AppDir('AppsLauncher', 'exit', ExitCode=ExitCode), mode)

if False:
#if not mode['test']:
    main = pyuac.main_requires_admin(main)

if __name__ == '__main__':
    main()

'''
读取到整合后：{'AppName':'G:/example/example.exe'}     AppPath
文件中：{'AppName':'example/example.exe'}     AppDir
设置保存方法：{'Name':'DefaultValue'}    settings     {'打开不关闭':False,'确认删除':True}
应用数据保存路径：./data

所有文件路径拼接用'/'
'''

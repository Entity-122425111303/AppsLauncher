from appcls import AppDir
import json, os, re


# noinspection
def path_switch(dir1: AppDir, mode: dict):  # type: ignore
    '''
    :param dir1:  'app' 'exit' 'settings'
    '''
    DefaultSettings = {'打开不关闭': False, '确认删除': True}
    match dir1:
        case AppDir('AppsLauncher', 'app', env) if env['operate'] == 'open':  # 打开应用
            try:
                print(f'opening {env["Name"]}')
                AppPath = path_switch(AppDir("AppsLauncher", 'app', operate='get'), mode)
                os.startfile(AppPath[env["Name"]])
                return True
            except:
                print('fail!')
                return False
        case AppDir('AppsLauncher', 'app', env) \
                if env['operate'] == 'insert' and env['NewName'] and env['NewPath']:  # 增加应用
            try:
                AppPath = path_switch(AppDir("AppsLauncher",
                                             'app',
                                             operate='get',
                                             drives=re.split(':', env["NewPath"])[0],
                                             ), mode)
            except ValueError as e:
                path_switch(AppDir("AppsLauncher", 'exit', ErrorCode=1, ErrorInfo=e), mode)
            if env['NewName'] in AppPath:
                print('the app has already been created')
            else:
                AppPath[env['NewName']] = re.split(':/', env["NewPath"])[-1]
                path_switch(AppDir('AppsLauncher',
                                   'app',
                                   operate='write',
                                   drives=re.split(':', env["NewPath"])[0],
                                   AppPathDict=AppPath,
                                   ), mode)
        case AppDir('AppsLauncher', 'app', env) \
                if env['operate'] == 'edit' and env['NewName'] and env['NewPath'] and env['InitialName']:  # 编辑应用
            if not (mode['--T-AddApps'] and any((env['Name'] == 'app1', env['Name'] == 'app2', env['Name'] == 'app3'))):
                AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), mode)
                InitialDrives = re.split(':', AppPath[env['InitialName']])[0]
                AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get', drives=InitialDrives), mode)
                AppPath.pop(env['InitialName'])
                path_switch(AppDir('AppsLauncher',
                                   'app',
                                   operate='write',
                                   drives=InitialDrives,
                                   AppPathDict=AppPath,
                                   ), mode)
            NewDrives = re.split(':', env['NewPath'])[0]
            AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get', drives=NewDrives), mode)
            AppPath[env['NewName']] = re.split(':', env['NewPath'])[-1]
            path_switch(AppDir('AppsLauncher',
                                'app',
                                operate='write',
                                drives=NewDrives,
                                AppPathDict=AppPath,
                                ), mode)
        case AppDir('AppsLauncher', 'app', env) if env['operate'] == 'delete' and env['Name']:  # 删除应用
            if not (mode['--T-AddApps'] and any((env['Name'] == 'app1', env['Name'] == 'app2', env['Name'] == 'app3'))):
                AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), mode)
                drives = re.split(':', AppPath[env['Name']])[0]
                AppPath = path_switch(AppDir('AppsLauncher',
                                             'app',
                                             operate='get',
                                             drives=drives,
                                             add_drive=False,
                                             ), mode)
                AppPath.pop(env['Name'])
                path_switch(AppDir('AppsLauncher', 'app', operate='write', drives=drives, AppPathDict=AppPath), mode)
        case AppDir('AppsLauncher', 'app', env) if env['operate'] == 'get':  # 获取应用字典
            AppPath: dict = {}
            for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                p = x + r':/AppsLauncher/data/AppPath.json'
                if os.path.exists(p):
                    with open(p, 'r', encoding='utf8') as f:
                        AppDir1: dict = json.load(f)
                    for z, y in AppDir1.items():
                        AppPath[z] = x + ':/' + y
            return AppPath
        case AppDir('AppsLauncher', 'app', env) if env['operate'] == 'get' and env['drives']:  # 获取指定盘应用字典
            AppPath: dict = {}
            try:
                env['add_drive']
            except KeyError:
                env['add_drive'] = True
            for x in env['drives']:
                p = x + r':/AppsLauncher/data/AppPath.json'
                if os.path.exists(p):
                    with open(p, 'r', encoding='utf8') as f:
                        AppDir1: dict = json.load(f)
                    for z, y in AppDir1.items():
                        if env['add_drive']:
                            AppPath[z] = x + ':/' + y
            if AppPath:
                return AppPath
            else:
                raise ValueError('incorrect drives')
        case AppDir('AppsLauncher', 'app', env) \
                if all((env['operate'] == 'write', env['drives'], isinstance(env['AppPathDict'], dict))):  # 写入指定盘应用字典
            os.makedirs(env['drives'] + r':/AppsLauncher/data', exist_ok=True)
            p = env['drives'] + r':/AppsLauncher/data/AppPath.json'
            try:
                with open(p, 'w', encoding='utf8') as f:
                    json.dump(env['AppPathDict'], f, ensure_ascii=False, indent=4)
            except:
                raise ValueError('incorrect drives')
        case AppDir('AppsLauncher', 'exit', env) if env:  # 退出
            if env['ExitCode'] == 0:
                exit(0)
            else:
                if env['ErrorInfo']:
                    exit(f'{env["ErrorInfo"]}')
                elif type(env['ExitCode']) is str:
                    exit(env['ExitCode'])
                else:
                    exit(env['ExitCode'])
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'edit':  # 修改设置
            with open('./data/settings.json', 'r', encoding='utf8') as f:
                setings: dict = json.load(f)
            for x, y in env.items():
                if x != 'operate':
                    setings[x] = y
            with open('./data/settings.json', 'w', encoding='utf8') as f:
                json.dump(setings, f, ensure_ascii=False, indent=4)
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'open':  # 打开设置
            raise SyntaxError(f'Invalid app path {dir1.get_fulldir()}   (尚未支持此语句)')
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'get':  # 获取设置
            with open('./data/settings.json', 'r', encoding='utf8') as f:
                settings = json.load(f)
            try:
                return settings[env['Name']]
            except:
                try:
                    return DefaultSettings[env['Name']]
                except:
                    return None
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'getfull':  # 获取全部设置
            with open('./data/settings.json', 'r', encoding='utf8') as f:
                settings = json.load(f)
            return settings
        case _:
            raise SyntaxError(f'Invalid app path {dir1.get_fulldir()}')


if __name__ == '__main__':

    class TestError(Exception):
        pass

    try:
        raise TestError('test')
    except TestError as e:
        path_switch(AppDir('AppsLauncher', 'exit', ExitCode='O.o', ErrorInfo=e), mode={'test': True})

from appcls import AppDir


def path_switch(dir1: AppDir):
    match dir1:
        case AppDir('AppsLauncher', 'open', env) if env:  # 打开应用
            print(f'open {env["AppName"]}')
        case AppDir('AppsLauncher', 'exit', env) if env:  # 退出
            if env['ExitCode'] == 0:
                exit(0)
            else:
                if env['Error'] and env['ErrorInfo']:
                    print(f'error {env["Error"]} {env["ErrorInfo"]}')
                    exit(1)
                elif (not env['Error']) and env['ErrorInfo']:
                    exit(env['ErrorInfo'])
                elif type(env['ErrorCode']) is str:
                    exit(env['ErrorCode'])
                else:
                    exit(env['ExitCode'])
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'edit':  # 修改设置
            print(env)
        case AppDir('AppsLauncher', 'settings', env) if env['operate'] == 'open':  # 打开设置
            print('settings')
        case _:
            raise SyntaxError(f'Invalid app path {dir1.get_fulldir()}')


if __name__ == '__main__':
    path_switch(AppDir('AppsLauncher', 'exit', ExitCode='0', Error=True))

from collections import defaultdict


class AppDir:

    __match_args__ = ('__obj__', '__AppDir__', '__query_dict__')

    def __init__(self, arg, path, **query):
        """
        构造 AppDir 对象。
        用法：AppDir("AppsLauncher", "open", AppName="test")  # 从参数构建
        :param arg:"AppsLauncher"
        """
        # 多个参数：scheme, path, 以及可能的查询参数
        self.__obj__ = arg
        self.__AppDir__ = path
        # 将查询参数转换为适当的类型（与字符串解析时行为一致）
        self.__query_dict__ = defaultdict(lambda: None)
        for key, val in query.items():
            self.__query_dict__[key] = val
        self.__query__ = []  # 保留兼容

    @property
    def get_obj(self):
        return self.__obj__

    @property
    def get_dir(self):
        return self.__AppDir__

    @property
    def get_query_dict(self):
        return self.__query_dict__

    def get_fulldir(self):
        """重新构造完整的 URL 字符串，并对值进行 URL 编码"""
        return [self.__obj__, self.__AppDir__, self.__query_dict__]

    def __str__(self):
        return str([self.__obj__, self.__AppDir__, dict(self.__query_dict__)])

    def __bool__(self):
        return bool(self.__obj__ and self.__AppDir__)

    def __eq__(self, other):
        return str(self) == str(other)

    def __iter__(self):
        yield from [self.__obj__, self.__AppDir__, self.__query_dict__]

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.get_fulldir()}>'


if __name__ == '__main__':
    s = AppDir('AppsLauncher', 'open', AppName='app', AppPath='path')
    print(s.get_obj, s.get_dir, dict(s.get_query_dict))
    print(s)


import os, sys, PyQt5

# 获取 PyQt5 包所在的目录
pyqt_path = os.path.dirname(PyQt5.__file__)
# Qt5 插件通常位于 PyQt5/Qt5/plugins/ 或 PyQt5/Qt/plugins/
plugins_candidate = os.path.join(pyqt_path, 'Qt5', 'plugins')
if not os.path.isdir(plugins_candidate):
    # 尝试另一种常见结构
    plugins_candidate = os.path.join(pyqt_path, 'Qt', 'plugins')

if os.path.isdir(plugins_candidate):
    os.environ['QT_PLUGIN_PATH'] = plugins_candidate
else:
    sys.exit("Warning: Could not locate Qt plugins directory.")

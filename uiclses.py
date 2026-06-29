import functools

from PyQt5 import QtWidgets, QtCore
from choose import choose_file
from operatefuncs import *


class Ui_Dialog(QtWidgets.QDialog):
    '''
    result_data:{'InitialName': ..., 'InitialPath': ..., 'Name': ..., 'Path': ...}
    '''
    def setupUi(self, mode, Dialog, window_type: str = 'insert', *, text1: str = None, text2: str = None):
        self.mode = mode
        self.result_data = None
        self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
        self.Dialog = Dialog
        self.window_type = window_type
        self.text1 = text1
        self.text2 = text2
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 97)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 291, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 371, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 30, 291, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 70, 291, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_3.clicked.connect(self.view)

        self.lineEdit.textChanged.connect(self.text_changed1)
        self.lineEdit_2.textChanged.connect(self.text_changed2)

        if window_type == 'edit':
            self.lineEdit.setText(text1)
            self.lineEdit_2.setText(text2)

        self.pushButton.clicked.connect(self.OK)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "浏览"))
        self.pushButton_3.setShortcut(_translate("Dialog", "V"))
        self.label_2.setText(_translate("Dialog", "应用路径:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "请输入应用路径"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.setShortcut(_translate("Dialog", "C"))
        self.label.setText(_translate("Dialog", "应用名:"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入应用名"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton.setShortcut(_translate("Dialog", "O"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))

        self.label_3.hide()
        self.label_4.hide()
        self.label_3.setStyleSheet('color:red;')
        self.label_4.setStyleSheet('color:red;')

    def text_changed1(self):
        self.label_3.hide()

    def text_changed2(self):
        self.label_4.hide()

    def view(self):
        if choose := choose_file([('可执行文件', '*.bat;*.exe'), ('所有文件', '*.*')]):
            self.lineEdit_2.setText(choose)
            self.lineEdit.setText(choose.split('/')[-1])

    def OK(self):
        error = False
        self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
        if not self.lineEdit.text():
            self.change_text1('此栏不为空!')
            error = True
        if not self.lineEdit_2.text():
            self.change_text2('此栏不为空!')
            error = True
        elif not os.path.exists(self.lineEdit_2.text()):
            if not self.mode['test']:
                self.change_text2('路径无效!')
                error = True
        elif os.path.isdir(self.lineEdit_2.text()):
            if not self.mode['test']:
                self.change_text2('路径无效!')
                error = True
        if all((self.window_type == 'edit',
                self.lineEdit_2.text() == self.text2,
                self.lineEdit.text() == self.text1,
                )):
            if self.lineEdit_2.text() == self.text2:
                self.change_text2('未更改!')
                error = True
            if self.lineEdit.text() == self.text1:
                self.change_text1('未更改!')
                error = True
        if all((self.lineEdit.text() in self.AppPath.keys(), self.window_type == 'insert')):
            self.change_text1('应用名已存在!')
            error = True
        if not error:
            self.result_data = {'InitialName': self.text1,
                                'InitialPath': self.text2,
                                'Name': self.lineEdit.text(),
                                'Path': self.lineEdit_2.text(),
                                }
            self.accept()
            self.Dialog.close()

    def change_text1(self, text: str):
        self.label_3.setText(text)
        self.label_3.show()

    def change_text2(self, text: str):
        self.label_4.setText(text)
        self.label_4.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, mode):
        self.windowopen = False
        self.mode = mode
        self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 391, 251))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 40, 107, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 90, 107, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 140, 107, 23))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setAcceptDrops(False)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 190, 107, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 290, 391, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 240, 107, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 310, 391, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.open)
        self.pushButton_5.clicked.connect(self.insert)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.edit)
        self.pushButton_8.clicked.connect(self.link)

        self.change_btn_enabled_true = functools.partial(self.change_btn_enabled, a0=True)
        self.listWidget.itemClicked.connect(self.change_btn_enabled_true)

        self.checkBox_2.clicked.connect(self.checkbox2checked)
        self.checkBox.clicked.connect(self.checkboxchecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AppsLauncher"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(True)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("MainWindow", "Open"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "O"))
        self.pushButton_5.setText(_translate("MainWindow", "Insert"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "I"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "D"))
        self.pushButton_7.setText(_translate("MainWindow", "Edit"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "E"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Esc"))
        self.checkBox.setText(_translate("MainWindow", "打开应用后不关闭此窗口"))
        self.pushButton_8.setText(_translate("MainWindow", "Link"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "L"))
        self.checkBox_2.setText(_translate("MainWindow", "不再确认删除"))

        self.change_btn_enabled(False)

        self.pushButton_8.hide()

        self.checkBox.setChecked(path_switch(AppDir('AppsLauncher',
                                                    'settings',
                                                    operate='get',
                                                    Name='打开不关闭',
                                                    ), self.mode))
        self.checkBox_2.setChecked(not path_switch(AppDir('AppsLauncher',
                                                          'settings',
                                                          operate='get',
                                                          Name='确认删除',
                                                          ), self.mode))

    def change_btn_enabled(self, a0):
        self.pushButton_4.setEnabled(a0)
        self.pushButton_6.setEnabled(a0)
        self.pushButton_7.setEnabled(a0)
        self.pushButton_8.setEnabled(a0)

    def open(self):
        print_logs(self.listWidget.currentItem().text())
        path_switch(AppDir('AppsLauncher', 'app', Name=self.listWidget.currentItem().text(), operate='open'), self.mode)
        if not self.checkBox.isChecked():
            self.MainWindow.close()

    def insert(self):
        if not self.windowopen:
            self.windowopen = True
            Dialog = QtWidgets.QDialog()
            ui2 = Ui_Dialog()
            ui2.setupUi(self.mode, Dialog)
            Dialog.exec()
            print_logs(ui2.result_data)
            if ui2.result_data:
                path_switch(AppDir('AppsLauncher',
                                   'app',
                                   operate='insert',
                                   NewName=ui2.result_data['Name'],
                                   NewPath=ui2.result_data['Path'],
                                   ), self.mode)
                self.add_choice_to_viewlist({ui2.result_data['Name']: ui2.result_data['Path']})
            else:
                print_logs('no input')
            self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
            self.windowopen = False
    def delete(self):
        if not self.windowopen:
            self.windowopen = True
            if path_switch(AppDir('AppsLauncher', 'settings', operate='get', Name='确认删除'), self.mode):
                m = QtWidgets.QDialog()
                ui2 = Um()
                ui2.setupUi(m)
                m.exec()
                print_logs(ui2.returndata)
                if ui2.returndata is not None:
                    path_switch(AppDir('AppsLauncher',
                                       'app',
                                       operate='delete',
                                       Name=self.listWidget.currentItem().text(),
                                       ), self.mode)
                    self.listWidget.takeItem(self.listWidget.currentRow())
                    if ui2.returndata:
                        path_switch(AppDir("AppsLauncher", 'settings', operate='edit', 确认删除=False), self.mode)
                        self.checkBox_2.setChecked(True)
            else:
                path_switch(AppDir('AppsLauncher',
                                   'app',
                                   operate='delete',
                                   Name=self.listWidget.currentItem().text(),
                                   ), self.mode)
                self.listWidget.takeItem(self.listWidget.currentRow())
            self.change_btn_enabled(False)
            self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
            self.windowopen = False
    def edit(self):
        if not self.windowopen:
            self.windowopen = True
            Dialog = QtWidgets.QDialog()
            ui2 = Ui_Dialog()
            if self.mode['--T-AddApps'] and any((self.listWidget.currentItem().text() == 'app1', self.listWidget.currentItem().text() == 'app2', self.listWidget.currentItem().text() == 'app3')):
                text2 = 'dir'
            else:
                text2 = path_switch(AppDir('AppsLauncher', 'app', operate='get'),
                                    self.mode)[self.listWidget.currentItem().text()]
            ui2.setupUi(self.mode, Dialog, window_type='edit', text1=self.listWidget.currentItem().text(), text2=text2)
            Dialog.exec()
            print_logs(ui2.result_data)
            if ui2.result_data:
                path_switch(AppDir('AppsLauncher',
                                   'app',
                                   operate='edit',
                                   NewName=ui2.result_data['Name'],
                                   NewPath=ui2.result_data['Path'],
                                   InitialName=ui2.result_data['InitialName'],
                                   ), self.mode)
                CurrentLine = self.listWidget.currentItem()
                CurrentLine.setText(ui2.result_data['Name'])
            self.AppPath = path_switch(AppDir('AppsLauncher', 'app', operate='get'), self.mode)
            self.windowopen = False

    def add_choice_to_viewlist(self, AppDict: dict[str, AppDir | str]):
        self.listWidget.addItems(AppDict.keys())

    def checkbox2checked(self):
        path_switch(AppDir("AppsLauncher", 'settings', operate='edit', 确认删除=not self.checkBox_2.isChecked()), self.mode)

    def checkboxchecked(self):
        path_switch(AppDir("AppsLauncher", 'settings', operate='edit', 打开不关闭=self.checkBox.isChecked()), self.mode)

    def link(self):
        pass


class Um(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.returndata = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 190)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 301, 91))
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 130, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 100, 211, 20))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.pushButton_4.clicked.connect(self.OK)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**确定删除？**"))
        self.pushButton_4.setText(_translate("Dialog", "OK"))
        self.pushButton_4.setShortcut(_translate("Dialog", "O"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setShortcut(_translate("Dialog", "C"))
        self.checkBox_2.setText(_translate("Dialog", "下次不再提示"))

    def OK(self):
        self.returndata = self.checkBox_2.isChecked()
        self.accept()
        self.Dialog.close()

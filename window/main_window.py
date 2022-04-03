from PySide6.QtWidgets import QMainWindow, QAbstractItemView
from PySide6.QtCore import QStringListModel, QItemSelectionModel

from ui.main_ui import Ui_MainWindow
from utils.config import Config


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 初始化单选框
        self.suffix_false.setChecked(True)
        self.iteration_false.setChecked(True)

        # 初始化文件列表
        # 创建mode
        self.file_list_model = QStringListModel()
        # 添加的数组数据
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        # 将数据设置到model
        self.file_list_model.setStringList(self.qList)
        # 绑定 listView 和 model
        self.file_list.setModel(self.file_list_model)
        # 多选
        self.file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 不能对表格进行修改（双击重命名等）
        self.file_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 初始化选择列表
        # 创建mode
        self.select_list_model = QStringListModel()
        # 绑定 listView 和 model
        self.select_list.setModel(self.select_list_model)
        # 多选
        self.select_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 不能对表格进行修改（双击重命名等）
        self.select_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 后缀列表初始化
        # 初始化列表
        self.suffix_select.addItems(Config().get()['suffix_list'])
        # 列表可输入
        self.suffix_select.setEditable(True)
        # 设置最大长度
        self.suffix_select.lineEdit().setMaxLength(8)

        # 按钮集中绑定
        # 绑定函数
        self.select_in.clicked.connect(self.select_in_onclick)
        self.select_out.clicked.connect(self.select_out_onclick)
        self.all_select.clicked.connect(self.all_select_onclick)

    def select_in_onclick(self):
        selected = self.file_list.selectedIndexes()
        slist = []
        for i in selected:
            item = i.row()
            inf = f"Pos:{item + 1},data: {self.file_list_model.stringList()[item]}"
            print(inf)
            row = self.select_list_model.rowCount()
            word = self.file_list_model.stringList()[item]
            self.select_list_model.insertRow(row)
            self.select_list_model.setData(self.select_list_model.index(row),
                                           word)
            slist.append(item)
        for i in slist[::-1]:
            self.file_list_model.removeRow(i)

    def select_out_onclick(self):
        selected = self.select_list.selectedIndexes()
        slist = []
        for i in selected:
            item = i.row()
            inf = f"Pos:{item + 1},data: {self.select_list_model.stringList()[item]}"
            print(inf)
            row = self.file_list_model.rowCount()
            word = self.select_list_model.stringList()[item]
            self.file_list_model.insertRow(row)
            self.file_list_model.setData(self.file_list_model.index(row), word)
            slist.append(item)
        for i in slist[::-1]:
            self.select_list_model.removeRow(i)

    def all_select_onclick(self):
        print(self.suffix_select.currentText())
        for i in range(3):
            self.file_list.selectionModel().setCurrentIndex(
                self.file_list_model.index(i), QItemSelectionModel.Select)

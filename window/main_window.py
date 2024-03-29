from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QFileDialog, QMessageBox
from PySide6.QtCore import QStringListModel, QItemSelectionModel, QRegularExpression, QUrl
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QDesktopServices, QIcon

from ui.main_ui import Ui_MainWindow
from utils.config import Config
from utils.file_control import FileControl
from utils.suffix_op import SuffixOperation
import resources.resources_rc


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 设置窗口名称及图标
        self.setWindowTitle('批量重命名助手')
        self.setWindowIcon(QIcon(':/images/icon.svg'))

        # 初始化FileControl类
        self.file_control = FileControl()
        # 初始化SuffixOperation类
        self.suffix_op = SuffixOperation()

        # 初始化Configs
        self.config = Config().get()

        # 初始化单选框
        self.suffix_false.setChecked(True)
        self.iteration_false.setChecked(True)

        # 初始化地址栏
        self.address.setText(
            self.file_control.getpath(
                start_from=self.config['path']['start_from'],
                start_path=self.config['path']['start_path']))

        # 初始化文件列表
        # 创建mode
        self.file_list_model = QStringListModel()
        # 获取文件列表
        files = self.file_control.getfiles(path=self.address.text())
        # 将数据设置到model
        self.file_list_model.setStringList(files)
        # 绑定 listView 和 model
        self.file_list.setModel(self.file_list_model)
        # 多选
        self.file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 不能对表格进行修改（双击重命名等）
        self.file_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 计算总计数量
        self.file_number.setText(f'总计：{self.file_list_model.rowCount()}')

        # 初始化选择列表
        # 创建mode
        self.select_list_model = QStringListModel()
        # 绑定 listView 和 model
        self.select_list.setModel(self.select_list_model)
        # 多选
        self.select_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 不能对表格进行修改（双击重命名等）
        self.select_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 计算总计数量
        self.select_number.setText(f'总计：{self.select_list_model.rowCount()}')

        # 后缀列表初始化
        # 初始化列表
        self.suffix_select.addItems(self.config['suffix_list'])
        # 列表可输入
        self.suffix_select.setEditable(True)
        # 设置最大长度
        self.suffix_select.lineEdit().setMaxLength(8)

        # 调整输入框限制
        # 后缀输入设置最大长度
        self.suffix.setMaxLength(8)
        # 后缀输入设置格式限制
        suffix_regExp = QRegularExpression('[a-zA-Z0-9\.]+')
        suffix_Validator = QRegularExpressionValidator(suffix_regExp)
        self.suffix.setValidator(suffix_Validator)
        # 序号输入设置仅输入数字
        self.no_input.setValidator(QIntValidator())

        # 集中绑定
        # 按钮
        self.select_in.clicked.connect(self.select_in_onclick)
        self.select_out.clicked.connect(self.select_out_onclick)
        self.all_select.clicked.connect(self.all_select_onclick)
        self.address_select.clicked.connect(self.address_select_onclick)
        self.iteration_true.toggled.connect(
            self.update_file_select_list_current)
        self.iteration_false.toggled.connect(
            self.update_file_select_list_current)
        self.rename.clicked.connect(self.rename_click)
        self.project_about.clicked.connect(self.project_about_click)
        self.revert.clicked.connect(self.revert_click)
        # 按键
        self.suffix_select.lineEdit().returnPressed.connect(
            self.all_select_onclick)
        self.address.returnPressed.connect(
            self.update_file_select_list_current)
        self.name_input.returnPressed.connect(self.rename_press)
        self.no_input.returnPressed.connect(self.rename_press)

    # 更新文件列表
    def update_file_select_list(self, files_address: str):
        # 获取文件列表
        # 不迭代
        if self.iteration_false.isChecked():
            files = self.file_control.getfiles(path=files_address)
        # 迭代
        else:
            files = self.file_control.getfiles(path=files_address,
                                               iteration=True)
        # 将数据设置到model
        self.file_list_model.setStringList(files)
        self.select_list_model.setStringList([])

        # 更新总计数量
        self.file_number.setText(f'总计：{self.file_list_model.rowCount()}')
        self.select_number.setText(f'总计：{self.select_list_model.rowCount()}')

    # 使用当前地址更新文件列表
    def update_file_select_list_current(self):
        self.update_file_select_list(self.address.text())

    # 点击地址选择按钮
    def address_select_onclick(self):
        files_address = QFileDialog.getExistingDirectory(
            self, "选择文件路径",
            self.file_control.getpath(
                start_from=self.config['path']['start_from'],
                start_path=self.config['path']['start_path']))
        if files_address == '':
            return

        # 地址同步到地址栏
        self.address.setText(files_address)
        # 更新文件列表
        self.update_file_select_list(files_address)

    # 点击选择文件按钮
    def select_in_onclick(self):
        selected = self.file_list.selectedIndexes()
        slist = []
        for i in selected:
            item = i.row()
            # inf = f"Pos:{item + 1},data: {self.file_list_model.stringList()[item]}"
            # print(inf)
            row = self.select_list_model.rowCount()
            word = self.file_list_model.stringList()[item]
            self.select_list_model.insertRow(row)
            self.select_list_model.setData(self.select_list_model.index(row),
                                           word)
            slist.append(item)
        for i in sorted(slist, reverse=True):
            # print(
            #     f'file remove pos:{i}, data:{self.file_list_model.stringList()[i]}'
            # )
            self.file_list_model.removeRow(i)

        # 更新总计数量
        self.file_number.setText(f'总计：{self.file_list_model.rowCount()}')
        self.select_number.setText(f'总计：{self.select_list_model.rowCount()}')

    # 点击取消选择文件按钮
    def select_out_onclick(self):
        selected = self.select_list.selectedIndexes()
        slist = []
        for i in selected:
            item = i.row()
            # inf = f"Pos:{item + 1},data: {self.select_list_model.stringList()[item]}"
            # print(inf)
            row = self.file_list_model.rowCount()
            word = self.select_list_model.stringList()[item]
            self.file_list_model.insertRow(row)
            self.file_list_model.setData(self.file_list_model.index(row), word)
            slist.append(item)
        for i in sorted(slist, reverse=True):
            # print(
            #     f'select remove pos:{i}, data:{self.select_list_model.stringList()[i]}'
            # )
            self.select_list_model.removeRow(i)
        # 更新总计数量
        self.file_number.setText(f'总计：{self.file_list_model.rowCount()}')
        self.select_number.setText(f'总计：{self.select_list_model.rowCount()}')

    # 点击全选按钮
    def all_select_onclick(self):
        # print(self.suffix_select.currentText())
        suffix = self.suffix_select.currentText()
        self.file_list.clearSelection()
        if self.suffix_op.pre_operate(suffix) == '.*':
            self.file_list.selectAll()
        else:
            pattern = self.suffix_op.get_regular_expression(suffix)
            for i, file in enumerate(self.file_list_model.stringList()):
                if pattern.search(file):
                    self.file_list.selectionModel().setCurrentIndex(
                        self.file_list_model.index(i),
                        QItemSelectionModel.Select)
        # 删除suffix_select中之前添加的内容
        for i in range(self.suffix_select.count()):
            if self.suffix_select.itemText(i) not in self.config[
                    'suffix_list'] and self.suffix_select.itemText(
                        i) != suffix:
                self.suffix_select.removeItem(i)
                break

    # 重命名
    def rename_click(self):
        success = self.file_control.rename(
            address=self.address.text(),
            iteration=False if self.iteration_false.isChecked() else True,
            file_list=self.select_list_model.stringList(),
            name=self.name_input.text(),
            no=self.no_input.text(),
            suffixif=False if self.suffix_false.isChecked() else True,
            suffix=self.suffix_op.pre_operate(self.suffix.text()))
        if success:
            print("success")
            QMessageBox.information(
                self, '成功',
                f'批量重命名完成！\n完成数量: {self.select_list_model.rowCount()}')
        else:
            msg = QMessageBox.critical(
                self, '错误',
                '批量重命名失败，可能存在如下问题！\n1. 命名过程中存在重名问题\n2. 存在命名不合法问题\n是否需要撤销出错前已完成的操作?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg == QMessageBox.Yes:
                success = self.file_control.revert()
                if success:
                    QMessageBox.information(self, '成功', f'撤销成功！')

        # 运行结束自动刷新
        self.update_file_select_list_current()

    # 回车键重命名需弹窗确认
    def rename_press(self):
        msg = QMessageBox.question(self, '重命名', '确认开始批量重命名？',
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes)
        if msg == QMessageBox.Yes:
            self.rename_click()

    # 撤销上一步操作需弹窗确认
    def revert_click(self):
        if self.file_control.can_revert():
            msg = QMessageBox.question(self, '撤销', '确认要撤销上一步操作吗？',
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
            if msg == QMessageBox.Yes:
                success = self.file_control.revert()
                if success:
                    QMessageBox.information(self, '成功', f'撤销成功！')
                # 运行结束自动刷新
                self.update_file_select_list_current()

    # 打开项目地址
    def project_about_click(self):
        QDesktopServices.openUrl(
            QUrl("https://github.com/Reilkay/file-rename-gui"))

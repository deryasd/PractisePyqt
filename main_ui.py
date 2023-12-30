# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 637)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        Form.setFont(font)
        Form.setStyleSheet("#info_frame {\n"
"    background-color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#info_frame QLabel,\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section\n"
" {\n"
"    font-family: Segoe UI Semibold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"    padding: 4px 5px;\n"
"    border: 1px solid #838383;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus\n"
" {\n"
"    border-color: #0055ff;\n"
"}\n"
"\n"
"QComboBox::drop-down { \n"
"    background: transparent; \n"
"    border: none;\n"
"    margin-right: 5px;\n"
"} \n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/expand_more.svg);\n"
"}\n"
"\n"
"#result_frame {\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    border: none;\n"
"    border-bottom:1px solid #d0c6ff;\n"
"    text-align:left;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    border-bottom:1px solid #d0c6ff;\n"
"    color: black;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"#function_frame QPushButton {\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"    background-color: #84e8f7;\n"
"}\n"
"\n"
"#function_frame QPushButton:hover {\n"
"    border-color: #4c96f7;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#function_frame #delete_btn {\n"
"    background-color: #ff8183;\n"
"}\n"
"\n"
"#function_frame #delete_btn:hover {\n"
"    border-color: #dc0004;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setContentsMargins(20, -1, 20, 20)
        self.gridLayout_5.setVerticalSpacing(15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_label = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_2.addWidget(self.title_label)
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
        self.function_frame = QtWidgets.QFrame(parent=Form)
        self.function_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.add_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.update_btn.setIconSize(QtCore.QSize(20, 20))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.select_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.select_btn.setIconSize(QtCore.QSize(20, 20))
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.search_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.clear_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.clear_btn.setIconSize(QtCore.QSize(20, 20))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.delete_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.delete_btn.setIconSize(QtCore.QSize(20, 20))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.gridLayout_5.addWidget(self.function_frame, 2, 0, 1, 1)
        self.result_frame = QtWidgets.QFrame(parent=Form)
        self.result_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.result_frame.setObjectName("result_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.result_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.result_frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(21)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(20, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.result_frame, 3, 0, 1, 1)
        self.info_frame = QtWidgets.QFrame(parent=Form)
        self.info_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout_6.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.info_frame)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.info_frame)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.info_frame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Students Information System"))
        self.title_label.setText(_translate("Form", "Ögrenci Bilgi Sistemi"))
        self.add_btn.setText(_translate("Form", "Ekle"))
        self.update_btn.setText(_translate("Form", "Güncelle"))
        self.select_btn.setText(_translate("Form", "Seç"))
        self.search_btn.setText(_translate("Form", "Ara"))
        self.clear_btn.setText(_translate("Form", "Temizle"))
        self.delete_btn.setText(_translate("Form", "Sil"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Öğrenci ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Soyad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Semt"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Şehir"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "EMail"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "fsdfsd"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "fasdfs"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "sdf"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "fsdf"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Öğrenci ID"))
        self.label_2.setText(_translate("Form", "Ad"))
        self.label_3.setText(_translate("Form", "Soyad"))
        self.label_4.setText(_translate("Form", "Şehir"))
        self.comboBox.setItemText(1, _translate("Form", "New Item"))
        self.comboBox.setItemText(2, _translate("Form", "New Item"))
        self.comboBox.setItemText(3, _translate("Form", "New Item"))
        self.comboBox.setItemText(4, _translate("Form", "New Item"))
        self.label_5.setText(_translate("Form", "Semt"))
        self.comboBox_2.setItemText(1, _translate("Form", "New Item"))
        self.comboBox_2.setItemText(2, _translate("Form", "New Item"))
        self.comboBox_2.setItemText(3, _translate("Form", "New Item"))
        self.comboBox_2.setItemText(4, _translate("Form", "New Item"))
        self.comboBox_2.setItemText(5, _translate("Form", "New Item"))
        self.label_6.setText(_translate("Form", "EMail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

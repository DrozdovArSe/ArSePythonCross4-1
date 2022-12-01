#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        self.label_error.setText('')
        self.label_max_el.setText('Максимальный элемент: ')
        self.label_sum.setText('Новый максимальный элемент: ')

    def solve(self):
        max_num, indi, indj = find_max(self.tableWidget)
        self.label_max_el.clear()
        self.label_max_el.setText('Максимальный элемент: ' + str(max_num))
        self.label_error.setText('')
        row = 0
        col = 0
        flag = False
        n = 0
        while row < 4:
            while col < 5:
                item = float(self.tableWidget.item(row, col).text())
                if row == indi and col == indj:
                    flag = True
                if (item%2 == 0) and flag == False:
                    n += 1
                col += 1
            col = 0
            row += 1
        new = max_num + n
        self.label_sum.setText('Новый максимальный элемент: ' + str(new))
        self.tableWidget.setItem(indi, indj, QTableWidgetItem(str(new)))


def find_max(table_widget):
    indi = 0
    indj = 0
    try:
        max_num = float(table_widget.item(indi, indj).text())
        row = 0
        col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number >= max_num:
                    max_num = number
                    indi = row
                    indj = col
                col += 1
            row += 1
            col = 0
        return [max_num, indi, indj]
    except Exception:
            return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

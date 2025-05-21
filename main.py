import sys
from curses.ascii import isdigit
from os.path import split

from PySide6.QtWidgets import *
from main_form import Ui_Form as Main_Form
from partners_form import Ui_Form as PartnerForm
import pymysql
import random


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="demo_ekz"
)


cursor = conn.cursor()
_id: None | int = None


class PartnerWindow(QWidget):
    def __init__(self):
        super(PartnerWindow, self).__init__()
        self.ui = PartnerForm()
        self.ui.setupUi(self)

        self.ui.btn_create.clicked.connect(self.create)
    
    def create(self):
        fields = self.get_fields()
        if not fields:
            QMessageBox.critical(self, "Ошибка ввода", "Необходимо заполнить все поля")
            return False
        stmt = ("INSERT INTO partners (`title`, `type`, `headmaster`, `mail`, `phone`, `address`, `INN`, `rating`) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(stmt, fields)
        conn.commit()
        QMessageBox.information(self, "", "Партнер добавлен")
        self.close()

    def update(self):
        global _id
        fields = self.get_fields()
        if not fields:
            QMessageBox.critical(self, "Ошибка ввода", "Необходимо заполнить все поля")
            return False
        stmt = ("UPDATE partners SET `title`=%s, `type`=%s, "
                "`headmaster`=%s, `mail`=%s, `phone`=%s, `inn=%s, "
                "`address=%s, `rating`=%s WHERE `id`=%s")
        cursor.execute(stmt, fields)
        conn.commit()
        QMessageBox.information(self, "", "Партнер обновлен")
        self.close()



    def get_fields(self):
        title = self.ui.edt_title.text()
        PType = self.ui.edt_type.text()
        headmaster = self.ui.edt_headmaster.text()
        mail = self.ui.edt_mail.text()
        phone = self.ui.edt_phone.text()
        inn = self.ui.edt_inn.text()
        address = self.ui.edt_address.text()
        rating = self.ui.edt_rating.text()

        if title == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле title не может быть пустым")
            return False
        if PType == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле PType не может быть пустым")
            return False
        if headmaster == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле headmaster не может быть пустым")
            return False
        if mail == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле mail не может быть пустым")
            return False
        if phone == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле phone не может быть пустым")
            return False
        if inn == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле inn не может быть пустым")
            return False
        if address == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле address не может быть пустым")
            return False
        if rating == "":
            QMessageBox.critical(self, "Ошибка ввода", "Поле rating не может быть пустым")
            return False
        try:
            rating = int(rating)
        except:
            QMessageBox.critical(self, "Ошибка ввода", "rating должен быть числом")
            return False

        return [title, PType, headmaster, mail, phone, inn, address, rating]


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.open_partner_form_create)
        self.ui.tableWidget.clicked.connect(self.open_partner_form_edit)

        self.refresh_data()
    
    def open_partner_form_create(self):
        self.ui.partner_form = PartnerWindow()
        self.ui.partner_form.show()
        self.ui.partner_form.ui.btn_create.show()
        self.ui.partner_form.ui.btn_edit.hide()
        # ----------
        self.ui.partner_form.closeEvent = self.refresh_data

    def open_partner_form_edit(self):
        self.ui.partner_form = PartnerWindow()
        self.ui.partner_form.show()
        self.ui.partner_form.ui.btn_create.hide()
        self.ui.partner_form.ui.btn_edit.show()

        global _id
        partner = self.ui.tableWidget.currentItem().text()
        PType, title = partner.split('\n')[0].split(' | ')
        title = title.split(' ')[0]
        print([title, PType])
        stmt = "SELECT * FROM partners WHERE `title`=%s AND `type`=%s"
        cursor.execute(stmt, [title, PType])
        partners = cursor.fetchone()
        self.ui.partner_form.ui.edt_title.setText(partners[1])
        self.ui.partner_form.ui.edt_type.setText(partners[2])
        self.ui.partner_form.ui.edt_headmaster.setText(partners[3])
        self.ui.partner_form.ui.edt_mail.setText(partners[4])
        self.ui.partner_form.ui.edt_phone.setText(partners[5])
        self.ui.partner_form.ui.edt_inn.setText(partners[6])
        self.ui.partner_form.ui.edt_address.setText(partners[7])
        self.ui.partner_form.ui.edt_rating.setText(str(partners[8]))
        # ----------
        self.ui.partner_form.closeEvent = self.refresh_data

    def refresh_data(self, event=None):
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(1)

        stmt = "SELECT * FROM partners ORDER BY rating DESC"
        cursor.execute(stmt)
        rows = cursor.fetchall()
        for row in rows:
            row_count = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.setRowCount(row_count + 1)
            text = f"""{row[2]} | {row[1]} \t\t\t\t{random.randrange(0, 16, 5)}%
{row[3]}
{row[5]}
Рейтинг: {row[8]}"""
            self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

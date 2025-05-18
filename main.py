from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem
import sys
from main_form import Ui_Form as Main_Form
from partners_form import Ui_Form as Partners_Form
from db import conn
import random


class PartnersWindow(QWidget):
    def __init__(self):
        super(PartnersWindow, self).__init__()
        self.ui = Partners_Form()
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.create_partner)
        self.ui.btn_edit.clicked.connect(self.update_partner)
    
    def create_partner(self):
        title = self.ui.edt_title.text()
        partner_type = self.ui.edt_type.text()
        headmaster = self.ui.edt_headmaster.text()
        mail = self.ui.edt_mail.text()
        phone = self.ui.edt_phone.text()
        address = self.ui.edt_address.text()
        INN = self.ui.edt_inn.text()
        rating = self.ui.edt_rating.text()
        cursor = conn.cursor()
        
        q = f"""INSERT INTO `partners` (`title`, `type`, `headmaster`, 
`mail`, `phone`, `address`, `INN`, `rating`) 
VALUES ('{title}', '{partner_type}', '{headmaster}', 
'{mail}', '{phone}','{address}', '{INN}', '{rating}')
        """
        res = cursor.execute(q)
        conn.commit()

        if res:
            print("insert success")
        else:
            print("error on insert")

    def update_partner(self):
        title = self.ui.edt_title.text()
        partner_type = self.ui.edt_type.text()
        headmaster = self.ui.edt_headmaster.text()
        mail = self.ui.edt_mail.text()
        phone = self.ui.edt_phone.text()
        address = self.ui.edt_address.text()
        INN = self.ui.edt_inn.text()
        rating = self.ui.edt_rating.text()
        cursor = conn.cursor()

        global p_id

        q = f"""UPDATE `partners` SET title = '{title}', type = '{partner_type}', 
headmaster = '{headmaster}', mail = '{mail}', phone = '{phone}', 
address = '{address}', INN = '{INN}', rating = {rating} 
WHERE id = {p_id}
        """
        res = cursor.execute(q)
        conn.commit()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.open_partners_form)
        self.ui.tableWidget.clicked.connect(self.open_partners_form_edit)
    
    def open_partners_form(self):
        self.ui.partners_form = PartnersWindow()
        self.ui.partners_form.show()

    def open_partners_form_edit(self):
        partner = self.ui.tableWidget.currentItem().text()
        tmp = partner.split('\n')
        headmaster = tmp[1].strip()
        p_type, title = tmp[0].split(' | ')
        title = title.rsplit(maxsplit=1)[0].strip()
        print(title)

        self.ui.partners_form = PartnersWindow()
        self.ui.partners_form.show()

        cursor = conn.cursor()
        q = f"SELECT * FROM `partners` where `type`='{p_type}' and `title`='{title}'"
        cursor.execute(q)
        partner = cursor.fetchone()
        print(partner)

        global p_id

        p_id = partner[0]
        self.ui.partners_form.ui.edt_title.setText(partner[1])
        self.ui.partners_form.ui.edt_type.setText(partner[2])
        self.ui.partners_form.ui.edt_headmaster.setText(partner[3])
        self.ui.partners_form.ui.edt_mail.setText(partner[4])
        self.ui.partners_form.ui.edt_phone.setText(partner[5])
        self.ui.partners_form.ui.edt_address.setText(partner[6])
        self.ui.partners_form.ui.edt_inn.setText(partner[7])
        self.ui.partners_form.ui.edt_rating.setText(str(partner[8]))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    cursor = conn.cursor()
    q = "SELECT * FROM partners"
    cursor.execute(q)
    rows = cursor.fetchall()
    # print(rows)
    
    window.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
    window.ui.tableWidget.verticalHeader().setDefaultSectionSize(100)
    window.ui.tableWidget.setRowCount(0)
    window.ui.tableWidget.setColumnCount(1)
    for row in rows:
        row_count = window.ui.tableWidget.rowCount()
        window.ui.tableWidget.setRowCount(row_count + 1)
        text = f"""{row[2]} | {row[1]}\t\t\t\t\t {random.randrange(0, 16, 5)}%
{row[3]}
{row[4]}
{row[5]}
Рейтинг: {row[-1]}"""
        window.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(text))

    sys.exit(app.exec())

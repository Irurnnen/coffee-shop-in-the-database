import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        id = self.FindID.text()
        result = cur.execute(
            """SELECT * FROM types_of_coffee WHERE ID = {}""".format(id))
        for answer in result:
            self.ID.setText(str(answer[0]))
            self.Name.setText(str(answer[1]))
            self.Level.setText(str(answer[2]))
            self.Bean.setText(str(answer[3]))
            self.Description.setText(str(answer[4]))
            self.Price.setText(str(answer[5]))
            self.Sizeq.setText(str(answer[6]))
            break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

import sys
# pip install pyqt5
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
# just change the name
from code_handle import show_chart
from gui import Ui_MainWindow

timer = QTimer()


def stop_update():
    timer.stop()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.thread = {}

        # khai bao nut an
        self.uic.Button_start_1.clicked.connect(self.show_diagram)
        self.uic.Button_start_2.clicked.connect(self.start_worker)

        self.uic.Button_stop_1.clicked.connect(stop_update)

        self.index = "T1"

    def closeEvent(self, event):
        print("close")
        stop_update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            print("enter press on keyboard")
            self.start_worker()

    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart(self.index))
        elif self.uic.screen is not None:
            timer.start(2000)

    def start_worker(self):
        input_index = self.uic.lineEdit_1.text()
        timer.stop()
        print("run script")
        self.uic.screen.itemAt(0).widget().deleteLater()
        self.index = input_index
        self.uic.screen.addWidget(show_chart(self.index))


# class show_chart(FigureCanvasQTAgg):
#     def __init__(self, index):
#         self.fig, self.ax = plt.subplots()
#         super().__init__(self.fig)
#         self.index = index
#         print("index", self.index)
#
#         plt.close()
#         plt.ion()
#
#         timer.timeout.connect(self.loop)
#         timer.start(2000)
#
#     def loop(self):
#         db = mysql.connector.connect(user='root', password='1234',
#                                      host='127.0.0.1', database='new_database')
#         # lenh chay
#         sql = "SELECT name,km FROM distance WHERE class = %s"
#         address = (self.index,)
#         # lệnh chạy code
#         mycursor = db.cursor()
#         mycursor.execute(sql, address)
#         results = mycursor.fetchall()
#         print(results)
#
#         name = []
#         km = []
#         for i in results:
#             name.append(i[0])
#             km.append(i[1])
#
#         # explode = (0.2, 0.1, 0)
#         print("name: ", name)
#         print("km: ", km)
#
#         self.ax.clear()
#         self.ax.pie(km, labels=name, autopct='%1.2f%%', shadow=True, startangle=90)  # , explode=explode

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
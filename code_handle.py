import mysql.connector
from PyQt5.QtCore import QTimer
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
timer = QTimer()

class show_chart(FigureCanvasQTAgg):
    def __init__(self, index):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.index = index
        print("index", self.index)

        plt.close()
        plt.ion()

        timer.timeout.connect(self.loop)
        timer.start(2000)

    def loop(self):
        db = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', database='new_database')
        # lenh chay
        sql = "SELECT name,km FROM distance WHERE class = %s"
        address = (self.index,)
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(sql, address)
        results = mycursor.fetchall()
        print(results)

        name = []
        km = []
        for i in results:
            name.append(i[0])
            km.append(i[1])

        # explode = (0.2, 0.1, 0)
        print("name: ", name)
        print("km: ", km)

        self.ax.clear()
        self.ax.pie(km, labels=name, autopct='%1.2f%%', shadow=True, startangle=90)  # , explode=explode
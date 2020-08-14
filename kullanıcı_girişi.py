import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
         
        h_box.addLayout(v_box)
        self.setLayout(h_box)
        h_box.addStretch()

        self.setWindowTitle("Kullanıcı Girişi")

        self.show()


app =QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())


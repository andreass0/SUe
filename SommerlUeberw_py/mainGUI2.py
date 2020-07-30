# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andreas\Documents\Woschitz\RWTplus\Bauphysik\FuE\SommerlUeberw\SommerlUeberw_py\mainGUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 420, 121, 21))
        self.label_8.setObjectName("label_8")
        self.idealLueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.idealLueftenInput.setGeometry(QtCore.QRect(120, 330, 113, 20))
        self.idealLueftenInput.setObjectName("idealLueftenInput")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 360, 121, 21))
        self.label_6.setObjectName("label_6")
        self.zeitschrittInput = QtWidgets.QLineEdit(self.centralwidget)
        self.zeitschrittInput.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.zeitschrittInput.setObjectName("zeitschrittInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 121, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 330, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 360, 121, 21))
        self.label_5.setObjectName("label_5")
        self.SonnenschutzInput = QtWidgets.QLineEdit(self.centralwidget)
        self.SonnenschutzInput.setGeometry(QtCore.QRect(120, 420, 113, 20))
        self.SonnenschutzInput.setObjectName("SonnenschutzInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 330, 121, 21))
        self.label_3.setObjectName("label_3")
        self.NachtlueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NachtlueftenInput.setGeometry(QtCore.QRect(120, 360, 113, 20))
        self.NachtlueftenInput.setObjectName("NachtlueftenInput")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 420, 121, 21))
        self.label_7.setObjectName("label_7")
        self.startSimulation = QtWidgets.QPushButton(self.centralwidget)
        self.startSimulation.setGeometry(QtCore.QRect(420, 510, 171, 41))
        self.startSimulation.setObjectName("startSimulation")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 100, 121, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.label_10.setObjectName("label_10")
        self.SeehoeheInput = QtWidgets.QLineEdit(self.centralwidget)
        self.SeehoeheInput.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.SeehoeheInput.setObjectName("SeehoeheInput")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 450, 121, 21))
        self.label_11.setObjectName("label_11")
        self.NatLueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NatLueftenInput.setGeometry(QtCore.QRect(120, 450, 113, 20))
        self.NatLueftenInput.setObjectName("NatLueftenInput")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 450, 121, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 480, 121, 21))
        self.label_13.setObjectName("label_13")
        self.MechLueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MechLueftenInput.setGeometry(QtCore.QRect(120, 480, 113, 20))
        self.MechLueftenInput.setObjectName("MechLueftenInput")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(250, 480, 121, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(250, 390, 121, 21))
        self.label_15.setObjectName("label_15")
        self.TaglueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TaglueftenInput.setGeometry(QtCore.QRect(120, 390, 113, 20))
        self.TaglueftenInput.setObjectName("TaglueftenInput")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 390, 121, 21))
        self.label_16.setObjectName("label_16")
        self.labelSimpara = QtWidgets.QLabel(self.centralwidget)
        self.labelSimpara.setGeometry(QtCore.QRect(40, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSimpara.setFont(font)
        self.labelSimpara.setObjectName("labelSimpara")
        self.labelStandort = QtWidgets.QLabel(self.centralwidget)
        self.labelStandort.setGeometry(QtCore.QRect(40, 80, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelStandort.setFont(font)
        self.labelStandort.setObjectName("labelStandort")
        self.labelHKLS = QtWidgets.QLabel(self.centralwidget)
        self.labelHKLS.setGeometry(QtCore.QRect(40, 300, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelHKLS.setFont(font)
        self.labelHKLS.setObjectName("labelHKLS")
        self.stopSimulation = QtWidgets.QPushButton(self.centralwidget)
        self.stopSimulation.setGeometry(QtCore.QRect(600, 510, 171, 41))
        self.stopSimulation.setObjectName("stopSimulation")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(370, 330, 121, 21))
        self.label_17.setObjectName("label_17")
        self.CustomSonnenschutzInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CustomSonnenschutzInput.setGeometry(QtCore.QRect(450, 360, 113, 20))
        self.CustomSonnenschutzInput.setObjectName("CustomSonnenschutzInput")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(580, 330, 121, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(580, 360, 121, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(370, 360, 121, 21))
        self.label_20.setObjectName("label_20")
        self.CustomLueftenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CustomLueftenInput.setGeometry(QtCore.QRect(450, 330, 113, 20))
        self.CustomLueftenInput.setObjectName("CustomLueftenInput")
        self.labelHKLS_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelHKLS_2.setGeometry(QtCore.QRect(380, 300, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelHKLS_2.setFont(font)
        self.labelHKLS_2.setObjectName("labelHKLS_2")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(370, 390, 121, 21))
        self.label_23.setObjectName("label_23")
        self.CustomInnereLastenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CustomInnereLastenInput.setGeometry(QtCore.QRect(450, 390, 113, 20))
        self.CustomInnereLastenInput.setObjectName("CustomInnereLastenInput")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(580, 390, 121, 21))
        self.label_24.setObjectName("label_24")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 520, 341, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(290, 30, 471, 251))
        self.graphWidget.setObjectName("graphWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append(randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

    #    self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    #def plot(self, hour, temperature):
    #    self.graphWidget.plot(hour, temperature)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SUe"))
        self.label_8.setText(_translate("MainWindow", "Sonnenschutz"))
        self.idealLueftenInput.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Nachtlüften"))
        self.zeitschrittInput.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Zeitschritt"))
        self.label_4.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.label_5.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.SonnenschutzInput.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "s"))
        self.label_3.setText(_translate("MainWindow", "ideal Lüften"))
        self.NachtlueftenInput.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.startSimulation.setText(_translate("MainWindow", "Start"))
        self.label_9.setText(_translate("MainWindow", "m"))
        self.label_10.setText(_translate("MainWindow", "Seehöhe"))
        self.SeehoeheInput.setText(_translate("MainWindow", "172"))
        self.label_11.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.NatLueftenInput.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "Nat. Lüftung"))
        self.label_13.setText(_translate("MainWindow", "Mech. Lüftung"))
        self.MechLueftenInput.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.label_15.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.TaglueftenInput.setText(_translate("MainWindow", "1"))
        self.label_16.setText(_translate("MainWindow", "Taglüften"))
        self.labelSimpara.setText(_translate("MainWindow", "Simulationsparameter"))
        self.labelStandort.setText(_translate("MainWindow", "Standort"))
        self.labelHKLS.setText(_translate("MainWindow", "HKLS-Steuerung (automatisch)"))
        self.stopSimulation.setText(_translate("MainWindow", "Stop"))
        self.label_17.setText(_translate("MainWindow", "Lüften"))
        self.CustomSonnenschutzInput.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.label_19.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))
        self.label_20.setText(_translate("MainWindow", "Sonnenschutz"))
        self.CustomLueftenInput.setText(_translate("MainWindow", "0"))
        self.labelHKLS_2.setText(_translate("MainWindow", "HKLS-Steuerung (aus Input Datei)"))
        self.label_23.setText(_translate("MainWindow", "Innere Lasten"))
        self.CustomInnereLastenInput.setText(_translate("MainWindow", "1"))
        self.label_24.setText(_translate("MainWindow", "1 = Ja //  0 = Nein"))


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

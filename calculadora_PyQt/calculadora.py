# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadoraQt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Dropbox/Mi PC (LAPTOP-CAT433DK)/Downloads/Calculator_30001.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(85, 255, 255);")
        self.boton_1 = QtWidgets.QPushButton(Form)
        self.boton_1.setGeometry(QtCore.QRect(40, 34, 56, 41))
        self.boton_1.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_1.setObjectName("boton_1")
        self.boton_2 = QtWidgets.QPushButton(Form)
        self.boton_2.setGeometry(QtCore.QRect(100, 34, 56, 41))
        self.boton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_2.setObjectName("boton_2")
        self.boton_3 = QtWidgets.QPushButton(Form)
        self.boton_3.setGeometry(QtCore.QRect(160, 34, 56, 41))
        self.boton_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_3.setObjectName("boton_3")
        self.boton_der = QtWidgets.QPushButton(Form)
        self.boton_der.setGeometry(QtCore.QRect(220, 40, 56, 61))
        self.boton_der.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 85, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_der.setObjectName("boton_der")
        self.boton_4 = QtWidgets.QPushButton(Form)
        self.boton_4.setGeometry(QtCore.QRect(40, 80, 56, 41))
        self.boton_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_4.setObjectName("boton_4")
        self.boton_7 = QtWidgets.QPushButton(Form)
        self.boton_7.setGeometry(QtCore.QRect(40, 130, 56, 41))
        self.boton_7.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_7.setObjectName("boton_7")
        self.boton_5 = QtWidgets.QPushButton(Form)
        self.boton_5.setGeometry(QtCore.QRect(100, 80, 56, 41))
        self.boton_5.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_5.setObjectName("boton_5")
        self.boton_x = QtWidgets.QPushButton(Form)
        self.boton_x.setGeometry(QtCore.QRect(40, 230, 56, 41))
        self.boton_x.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_x.setObjectName("boton_x")
        self.boton_division = QtWidgets.QPushButton(Form)
        self.boton_division.setGeometry(QtCore.QRect(100, 230, 56, 41))
        self.boton_division.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_division.setObjectName("boton_division")
        self.boton_suma = QtWidgets.QPushButton(Form)
        self.boton_suma.setGeometry(QtCore.QRect(40, 180, 56, 41))
        self.boton_suma.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_suma.setObjectName("boton_suma")
        self.boton_0 = QtWidgets.QPushButton(Form)
        self.boton_0.setGeometry(QtCore.QRect(100, 180, 56, 41))
        self.boton_0.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_0.setObjectName("boton_0")
        self.boton_8 = QtWidgets.QPushButton(Form)
        self.boton_8.setGeometry(QtCore.QRect(100, 130, 56, 41))
        self.boton_8.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_8.setObjectName("boton_8")
        self.boton_6 = QtWidgets.QPushButton(Form)
        self.boton_6.setGeometry(QtCore.QRect(160, 80, 56, 41))
        self.boton_6.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_6.setObjectName("boton_6")
        self.boton_100 = QtWidgets.QPushButton(Form)
        self.boton_100.setGeometry(QtCore.QRect(100, 280, 56, 41))
        self.boton_100.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_100.setObjectName("boton_100")
        self.boton_menos = QtWidgets.QPushButton(Form)
        self.boton_menos.setGeometry(QtCore.QRect(40, 280, 56, 41))
        self.boton_menos.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 170, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_menos.setObjectName("boton_menos")
        self.boton_ac = QtWidgets.QPushButton(Form)
        self.boton_ac.setGeometry(QtCore.QRect(160, 230, 56, 41))
        self.boton_ac.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_ac.setObjectName("boton_ac")
        self.boton_c = QtWidgets.QPushButton(Form)
        self.boton_c.setGeometry(QtCore.QRect(160, 180, 56, 41))
        self.boton_c.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_c.setObjectName("boton_c")
        self.boton_9 = QtWidgets.QPushButton(Form)
        self.boton_9.setGeometry(QtCore.QRect(160, 130, 56, 41))
        self.boton_9.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_9.setObjectName("boton_9")
        self.boton_punto = QtWidgets.QPushButton(Form)
        self.boton_punto.setGeometry(QtCore.QRect(220, 180, 56, 41))
        self.boton_punto.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 0, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_punto.setObjectName("boton_punto")
        self.boton_izq = QtWidgets.QPushButton(Form)
        self.boton_izq.setGeometry(QtCore.QRect(220, 110, 56, 61))
        self.boton_izq.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 0, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_izq.setObjectName("boton_izq")
        self.boton_salir = QtWidgets.QPushButton(Form)
        self.boton_salir.setGeometry(QtCore.QRect(160, 280, 56, 41))
        self.boton_salir.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 87 6pt \"Arial Black\";")
        self.boton_salir.setObjectName("boton_salir")
        self.boton_igual = QtWidgets.QPushButton(Form)
        self.boton_igual.setGeometry(QtCore.QRect(220, 230, 56, 91))
        self.boton_igual.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.boton_igual.setObjectName("boton_igual")
        self.valor = QtWidgets.QLabel(Form)
        self.valor.setGeometry(QtCore.QRect(40, 10, 233, 20))
        self.valor.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(170, 85, 0);")
        self.valor.setText("")
        self.valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor.setIndent(0)
        self.valor.setObjectName("valor")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 233, 20))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(170, 85, 0);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.boton_1.raise_()
        self.boton_2.raise_()
        self.boton_3.raise_()
        self.boton_der.raise_()
        self.boton_4.raise_()
        self.boton_7.raise_()
        self.boton_5.raise_()
        self.boton_x.raise_()
        self.boton_division.raise_()
        self.boton_suma.raise_()
        self.boton_0.raise_()
        self.boton_8.raise_()
        self.boton_6.raise_()
        self.boton_100.raise_()
        self.boton_menos.raise_()
        self.boton_ac.raise_()
        self.boton_c.raise_()
        self.boton_9.raise_()
        self.boton_punto.raise_()
        self.boton_izq.raise_()
        self.boton_salir.raise_()
        self.boton_igual.raise_()
        self.valor.raise_()

        self.retranslateUi(Form)
        self.boton_salir.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculadora"))
        self.boton_1.setText(_translate("Form", "1"))
        self.boton_1.setShortcut(_translate("Form", "1"))
        self.boton_2.setText(_translate("Form", "2"))
        self.boton_2.setShortcut(_translate("Form", "2"))
        self.boton_3.setText(_translate("Form", "3"))
        self.boton_3.setShortcut(_translate("Form", "3"))
        self.boton_der.setText(_translate("Form", "("))
        self.boton_der.setShortcut(_translate("Form", "("))
        self.boton_4.setText(_translate("Form", "4"))
        self.boton_4.setShortcut(_translate("Form", "4"))
        self.boton_7.setText(_translate("Form", "7"))
        self.boton_7.setShortcut(_translate("Form", "7"))
        self.boton_5.setText(_translate("Form", "5"))
        self.boton_5.setShortcut(_translate("Form", "5"))
        self.boton_x.setText(_translate("Form", "x"))
        self.boton_x.setShortcut(_translate("Form", "*"))
        self.boton_division.setText(_translate("Form", "÷"))
        self.boton_division.setShortcut(_translate("Form", "/"))
        self.boton_suma.setText(_translate("Form", "+"))
        self.boton_suma.setShortcut(_translate("Form", "+"))
        self.boton_0.setText(_translate("Form", "0"))
        self.boton_0.setShortcut(_translate("Form", "0"))
        self.boton_8.setText(_translate("Form", "8"))
        self.boton_8.setShortcut(_translate("Form", "8"))
        self.boton_6.setText(_translate("Form", "6"))
        self.boton_6.setShortcut(_translate("Form", "6"))
        self.boton_100.setText(_translate("Form", "%"))
        self.boton_menos.setText(_translate("Form", "-"))
        self.boton_menos.setShortcut(_translate("Form", "-"))
        self.boton_ac.setText(_translate("Form", "AC"))
        self.boton_c.setText(_translate("Form", "C"))
        self.boton_c.setShortcut(_translate("Form", "Esc"))
        self.boton_9.setText(_translate("Form", "9"))
        self.boton_9.setShortcut(_translate("Form", "9"))
        self.boton_punto.setText(_translate("Form", "."))
        self.boton_punto.setShortcut(_translate("Form", "."))
        self.boton_izq.setText(_translate("Form", ")"))
        self.boton_izq.setShortcut(_translate("Form", ")"))
        self.boton_salir.setText(_translate("Form", "SALIR"))
        self.boton_salir.setShortcut(_translate("Form", "C"))
        self.boton_igual.setText(_translate("Form", "="))
        self.boton_igual.setShortcut(_translate("Form", "Return"))
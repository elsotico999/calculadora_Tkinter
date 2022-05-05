import sys
from calculadora import *

class principal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.boton_0.clicked.connect(self.mostrar0)
        self.ui.boton_1.clicked.connect(self.mostrar1)
        self.ui.boton_2.clicked.connect(self.mostrar2)
        self.ui.boton_3.clicked.connect(self.mostrar3)
        self.ui.boton_4.clicked.connect(self.mostrar4)
        self.ui.boton_5.clicked.connect(self.mostrar5)
        self.ui.boton_6.clicked.connect(self.mostrar6)
        self.ui.boton_7.clicked.connect(self.mostrar7)
        self.ui.boton_8.clicked.connect(self.mostrar8)
        self.ui.boton_9.clicked.connect(self.mostrar9)
        self.ui.boton_menos.clicked.connect(self.mostrarmenos)
        self.ui.boton_suma.clicked.connect(self.mostrarmas)
        self.ui.boton_x.clicked.connect(self.mostrarmulti)
        self.ui.boton_division.clicked.connect(self.mostrardivi)
        self.ui.boton_100.clicked.connect(self.mostrarporc)
        self.ui.boton_der.clicked.connect(self.mostrarder)
        self.ui.boton_izq.clicked.connect(self.mostrarizq)
        self.ui.boton_punto.clicked.connect(self.mostrarpunto)
        self.ui.boton_igual.clicked.connect(self.mostrarigual)
        self.ui.boton_ac.clicked.connect(self.mostrarac)
        self.ui.boton_c.clicked.connect(self.mostrarcc)
        

    def mostrar0(self):
        entrada = self.ui.valor.text()
        entrada += "0"
        self.ui.valor.setText(entrada)

    def mostrar1(self):
        entrada = self.ui.valor.text()
        entrada += "1"
        self.ui.valor.setText(entrada)

    def mostrar2(self):
        entrada = self.ui.valor.text()
        entrada += "2"
        self.ui.valor.setText(entrada)

    def mostrar3(self):
        entrada = self.ui.valor.text()
        entrada += "3"
        self.ui.valor.setText(entrada)    

    def mostrar4(self):
        entrada = self.ui.valor.text()
        entrada += "4"
        self.ui.valor.setText(entrada)

    def mostrar5(self):
        entrada = self.ui.valor.text()
        entrada += "5"
        self.ui.valor.setText(entrada)

    def mostrar6(self):
        entrada = self.ui.valor.text()
        entrada += "6"
        self.ui.valor.setText(entrada)

    def mostrar7(self):
        entrada = self.ui.valor.text()
        entrada += "7"
        self.ui.valor.setText(entrada)

    def mostrar8(self):
        entrada = self.ui.valor.text()
        entrada += "8"
        self.ui.valor.setText(entrada)

    def mostrar9(self):
        entrada = self.ui.valor.text()
        entrada += "9"
        self.ui.valor.setText(entrada)

    def mostrarmenos(self):
        entrada = self.ui.valor.text()
        entrada += "-"
        self.ui.valor.setText(entrada)

    def mostrarmas(self):
        entrada = self.ui.valor.text()
        entrada += "+"
        self.ui.valor.setText(entrada)

    def mostrarmulti(self):
        entrada = self.ui.valor.text()
        entrada += "*"
        self.ui.valor.setText(entrada)

    def mostrardivi(self):
        entrada = self.ui.valor.text()
        entrada += "/"
        self.ui.valor.setText(entrada)

    def mostrarporc(self):
        entrada = self.ui.valor.text()
        try:
            self.an = (entrada+"/100")
            self.ui.valor.setText(self.an)
        except:
            self.ui.valor.setText("")

    def mostrarder(self):
        entrada = self.ui.valor.text()
        entrada += "("
        self.ui.valor.setText(entrada)

    def mostrarizq(self):
        entrada = self.ui.valor.text()
        entrada += ")"
        self.ui.valor.setText(entrada)

    def mostrarpunto(self):
        entrada = self.ui.valor.text()
        entrada += "."
        self.ui.valor.setText(entrada)
    
    def mostrarigual(self):
        entrada = self.ui.valor.text()
        try:
            ans= eval(entrada)
            self.ui.valor.setText(str(ans))
        except:
            self.ui.valor.setText("ERROR")

    def mostrarac(self):
        entrada = self.ui.valor.text()
        self.ui.valor.setText(entrada[:len(entrada)-1])
        
    def mostrarcc(self):
        entrada = self.ui.valor.text()
        self.ui.valor.setText(entrada[:len(entrada)-int(entrada)])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_calculadora = principal()
    mi_calculadora.show()
    sys.exit(app.exec_())


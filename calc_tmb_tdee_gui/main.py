import sys
from PyQt6.QtWidgets import QApplication, QWidget
import user_interface_calc  # Importa a interface gerada

class MainApp(QWidget, user_interface_calc.Ui_Calculadora_TMB_TDEE):  # Ajusta Ui_MainWindow se for outra classe
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a UI gerada
        self.setFixedSize(300, 600)
        self.calcular.clicked.connect(self.calc_tmb_tdee)   #Busca a função de calcular TMB / TDEE quando clickado
        self.input_idade.setPlaceholderText("em anos")
        self.input_altura.setPlaceholderText("em cms")
        self.input_peso.setPlaceholderText("em kgs (usar ponto para decimais)")


    def calc_tmb_tdee(self):

        peso = float(self.input_peso.text())            # Recebe o valor do campo peso e converte de texto para float
        idade = int(self.input_idade.text())            # Recebe o valor do campo idade e converte de texto para int
        altura = float(self.input_altura.text())        # Recebe o valor do campo altura e converte de texto para float
        genero = self.input_genero.currentText()        # Recebe o valor do campo genero (M ou F)

        atividade = self.input_atividade.currentText()  # Recebe o valor da atividade
        if atividade == 'Sedentario':
            atividade = 1.2
        elif atividade == 'Trabalho Sedentario + Desporto Pouco Intenso':
            atividade = 1.37
        elif atividade == 'Trabalho Sedentario + Desporto Muito Intenso':
            atividade = 1.55
        elif atividade == 'Trabalho Sedentario + Desporto de Alta Competição':
            atividade = 1.72
        elif atividade == 'Trabalho Sedentario + Culturismo Iniciante':
            atividade = 1.37
        elif atividade == 'Trabalho Sedentario + Culturismo Intermedio':
            atividade = 1.55
        elif atividade == 'Trabalho Fisico + Hipertrofia Intenso + Cardio 30 Min':
            atividade = 1.725
        elif atividade == 'Trabalho Fisico + Hipertrofia Intenso + Cardio 30 Min':
            atividade = 1.9

        #FORMULA PARA CALCULAR TMB
        if genero == 'Feminino':
            tmb = (10*peso)+(6.25*altura)-(5*idade)-161
        else:
            tmb = (10*peso)+(6.25*altura)-(5*idade)+5

        tdee = tmb * atividade

        objv = self.input_obj.currentText()              #Recebe o objetivo
        if objv == 'CUT - 350kcal':
            tdee = tdee-300
        elif objv == 'BODY RECOMP - 250kcal':
            tdee = tdee-250
        elif objv == 'BULK + 350 kcal':
            tdee = tdee+300
        
        self.output_resultado.setText(f"TMB: {tmb:2} kcals\nTDEE: {tdee:2} kcals")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())



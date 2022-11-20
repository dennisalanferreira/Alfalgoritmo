from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text() 

    categoria = ""
    if formulario.radioButton_2.isChecked() :
        print("Categoria Doações em Objetos selecionada")
        categoria ="Doações em Objetos"
    elif formulario.radioButton_3.isChecked() :
        print("Categoria Doações em Pix selecionada")
        categoria ="Doações em Pix"
   

    print("Produto:",linha1)
    print("Descricao:",linha2)
    print("Valor",linha3)
    print("Nome_do_doador:",linha4)
    print("Endereco:",linha5)
    print("Contato",linha6)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (Produto,Descricao,Valor,Nome_do_doador,Endereco,Contato,categoria) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()



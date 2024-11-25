import pandas as pd
import sqlite3

class Programa:
    def __init__(self, db = 'db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print("\n"
                "[1] - Create \n"
                "[2] - Read \n"
                "[3] - Update \n"
                "[4] - Delete \n"
                "[5] - Exit \n"
                "\n"
                )
            op = int(input("Escolha uma opção: "))
            match op:
                case 1:
                    self.menu_create()
                case 2:
                    print("Read")
                case 3:
                    print("Update")
                case 4:
                    print("Delete")
                case 5:
                    print("Você saiu!")
                    break
                case _:
                    print("Opção Invalida!")

    def create(self, tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome):
        cursor = self.conn.cursor()
        cursor.execute('''
                       INSERT INTO api_produto(tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome)
                       VALUES(?,?,?,?,?,?,?)
                       ''', (tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome))
        self.conn.commit()
        print("Produto cadastrado com sucesso!")
    
    def menu_create(self):
        print('\n'
              "1 - Titulo\n"
              "2 - Preco\n"
              "3 - Descrição\n"
              "4 - Imagem\n"
              "5 - Categoria\n"
              "6 - Classificação\n"
              "7 - Exibir(true/false)\n"          
              )
        
        tituloProduto = input("Título: ")
        preco = float(input("Preço: "))
        descricao = input("Descrição: ")
        catProduto = input("Categoria: ")
        self.create(tituloProduto, preco, descricao, catProduto,)

programa = Programa()
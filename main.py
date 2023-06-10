import sqlite3
from functions.user_db import register, login
from functions.skins_db import add_cart, list_cart, edit_cart, del_cart, search_skin

conn = sqlite3.connect('SorrisoSkins.db')
c = conn.cursor()

def menu():
    print("========= MENU =========")
    print("1. Cadastrar Usuário")
    print("2. Login")
    print("3. Sair do Sistema")
    print("========================")
def logged_menu():
    print("===== SorrisoSkins =) =====")
    print("1. Adicionar skin ao carrinho de compras")
    print("2. Listar skins do carrinho de compras")
    print("3. Editar o preço de uma skin do carrinho de compras")
    print("4. Remover uma skin do carrinho de compras")
    print("5. Buscar uma skin na loja")
    print("6. Logout")
    print("===========================")

def main():

    logado = False
    user_id = None

    while True:
        if not logado:
            menu()
            opc = int(input("Escolha uma opção: "))

            if opc == 1:
                username = input("Cadastre o usuário: ")
                password = input("Cadastre a senha: ")
                register(conn, username, password)
            elif opc == 2:
                username = input("Digite o nome de usuário: ")
                password = input("Digite a senha: ")
                user_id = login(conn, username, password)
                if user_id:
                    logado = True
                    print("Bem-vindo à SorrisoSkins! =)")
                else:
                    print("Falha no login. Usuário ou senha incorretos. Tente novamente.")
            elif opc == 3:
                print("Até logo mais! :)")
                print("==============================")
                print("©2023-2023, SorrisoSkins, Inc. ou suas afiliadas.")
                print("==============================")
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
            logged_menu()
            opc = int(input("Escolha uma opção: "))

            if opc == 1:
                skin_name = input("Digite o nome da skin: ")
                price = float(input("Digite o preço da skin: "))
                add_cart(conn, user_id, skin_name, price)
            elif opc == 2:
                list_cart(conn, user_id)
            elif opc == 3:
                skin_id = int(input("Digite o ID da skin que deseja editar o preço: "))
                new_price = float(input("Digite o novo preço da skin: "))
                edit_cart(conn, user_id, new_price, skin_id)
            elif opc == 4:
                skin_id = int(input("Digite o ID da skin que deseja remover do carrinho: "))
                del_cart(conn, user_id, skin_id)
            elif opc == 5:
                skin_busca = input("Digite a skin que deseja buscar: ")
                search_skin(conn, user_id, skin_busca)
            elif opc == 6:
                print("==============================")
                print("Fazendo logout...")
                logado = False
                user_id = None
            else:
                print("Opção inválida. Tente novamente.")
                
main()
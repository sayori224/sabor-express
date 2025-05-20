import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')

def exibir_opçoes():
    print('1. Cadastrar resturante')
    print('2. Listar resturantes')
    print('3. Ativar resturante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o app\n')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal ')
     main()

def opçao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    print('Listando todos os restaurantes\n')
            
for restaurante in restaurantes:
    print(f'.{restaurante}')

voltar_ao_menu_principal()

def escolher_opçao():
    try:

        opçao_escolhida = int(input('Escolha uma opção:'))


        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opçao_escolhida == 2:
            listar_restaurantes()
        elif opçao_escolhida == 3:
            print('Ativar restaurante')
        elif opçao_escolhida == 4:
            finalizar_app()
        else:
            opçao_invalida()
     
    except:
        opçao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == '__main__':
    main()
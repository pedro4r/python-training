from adicionar import adicionar_contato
from ver_contatos import ver_contatos
from editar_contato import editar_contato
from editar_favoritos import editar_favoritos
from deletar_contato import deletar_contato
from ver_favoritos import ver_favoritos

lista = []
while True:
  print("\nSelecione a opcao:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar Favoritos")
  print("4. Ver Favoritos")
  print("5. Editar Contato")
  print("6. Deletar Contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
   lista = adicionar_contato(lista)

  elif escolha == "2":
    ver_contatos(lista)

  elif escolha == "3":
    editar_favoritos(lista)

  elif escolha == "4":
    ver_favoritos(lista)

  elif escolha == "5":
    lista = editar_contato(lista)

  elif escolha == "6":
    lista = deletar_contato(lista)

  elif escolha == "7":
    break

print("Programa finalizado")
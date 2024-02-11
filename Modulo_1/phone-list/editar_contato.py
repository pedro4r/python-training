def editar_contato(lista):

  for i, contato in enumerate(lista):

    if contato["favorito"]:
      isFavorito = '⭐️'
    else:
      isFavorito = '-'

    print(f"[ {i+1} ] {isFavorito} {contato["nome"]} | {contato["telefone"]} | {contato["email"]}")

  escolha = input("Escolha qual contato quer editar: ")
  nome = input(f"Digite o novo nome do contato: ")
  telefone = input(f"Digite o novo telefone do contato: ")
  email = input(f"Digite o novo email do contato: ")

  contato_editado = {
    "nome": nome, 
    "telefone": telefone, 
    "email": email, 
    "favorito": lista[int(escolha)-1]["favorito"]
  }

  lista[int(escolha)-1] = contato_editado

  return lista
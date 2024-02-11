def deletar_contato(lista):

  for i, contato in enumerate(lista):

    if contato["favorito"]:
      isFavorito = '⭐️'
    else:
      isFavorito = '-'

    print(f"[ {i+1} ] {isFavorito} {contato["nome"]} | {contato["telefone"]} | {contato["email"]}")

  escolha = input("Escolha qual contato quer deletar: ")

  del lista[int(escolha)-1]

  return lista
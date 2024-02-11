def editar_favoritos(lista):

  for i, contato in enumerate(lista):

    if contato["favorito"]:
      isFavorito = '⭐️'
    else:
      isFavorito = '-'

    print(f"[ {i+1} ] {isFavorito} {contato["nome"]} | {contato["telefone"]} | {contato["email"]}")

  escolha = input("Escolha qual contato quer favoritar/desfavoritar: ")
  isFavorito = lista[int(escolha)-1]["favorito"]

  lista[int(escolha)-1]["favorito"] = not lista[int(escolha)-1]["favorito"]

  return lista
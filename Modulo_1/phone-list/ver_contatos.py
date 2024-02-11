def ver_contatos(lista):

  for contato in lista:
    if contato["favorito"]:
      isFavorito = '⭐️'
    else:
      isFavorito = '-'
    print(f"{isFavorito} {contato["nome"]} | {contato["telefone"]} | {contato["email"]}")

  return
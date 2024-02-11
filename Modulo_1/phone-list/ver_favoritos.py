def ver_favoritos(lista):
  for contato in lista:
    if contato["favorito"] == True:
      isFavorito = '⭐️'
      print(f"{isFavorito} {contato["nome"]} | {contato["telefone"]} | {contato["email"]}")
  return
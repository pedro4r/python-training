def adicionar_contato(lista):
  nome = input("Digite o nome da pessoa: ")
  telefone = input("Digite o telefone da pessoa: ")
  email = input("Digite o email da pessoa: ")
  print("Deseja favoritar o contato?")
  print("1. Sim")
  print("2. Não")
  favorito = input("Digite a sua escolha: ")
  favorito = True if favorito == '1' else False

  contato = {
    "nome": nome, 
    "telefone": telefone, 
    "email": email, 
    "favorito": favorito
  }
  lista.append(contato)
  print(f"O contato de {contato["nome"]} foi adicionada com sucesso!")

  return lista
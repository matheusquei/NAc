# -- Dados cadastrais

dados_cadastrais = [
  "Idade",
  "Sexo (M/F)",
  "Estado Civil (S/N)"
]

# -- Pergunta de inicialização

input("Farei algumas perguntas para você tudo bem? Pressione ENTER por gentileza")

# -- Dados com interação externa

dados_cadastrais.insert(0, int(input("Qual a sua idade?")))
dados_cadastrais.insert(1, input("Poderia me dizer qual é o seu sexo? Lembre-se de usar as letras M ou F"))
dados_cadastrais.insert(2, input("Agora por ultimo, por favor me informe qual é o seu estado civil? Por favor utilize as letras S ou N"))

# -- Condições

if dados_cadastrais[1].upper() == "F":
    print("Perfeito! Você tem direito a licença maternidade.")

elif dados_cadastrais[1].upper() =="M" and dados_cadastrais[0] >=20 and dados_cadastrais[0] <=39:
    print("Você é um trabalhador regular!")

elif dados_cadastrais[1].upper() =="M" and dados_cadastrais[0] >=40 and dados_cadastrais[0] <=60:
    print("Você pode trabalhar Home Office")

else:
    print("Não entendi a sua resposta")





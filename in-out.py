print ("Hello World")
print("hello \npulando linha")

nome = 'michel' #prenchendo variaveis
print(nome) #printando valores de variaveis

tipo = type(nome) #tipo da variavel
print(tipo) #print tipo

idade = 25 #variavel int
tipo_idade = type(idade) #recebe o tipo da variavel
print(tipo_idade) #imprime o tipo

altura = 1.69 #tipo float, usar ponto
tipo_altura = type(altura)
print(tipo_altura)

print(nome, 'tem', idade, 'anos') #imprimindo frases concatenadas!

print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' metros')#conversao de tipos

nome = input('escreva seu nome') #recebendo dados do usuario
idade = int(input('escreva sua idade'))#convertendo inputs
print(nome, 'tem', idade, 'anos') #imprimindo os dados
print (type(idade))# printando o tipo convertido
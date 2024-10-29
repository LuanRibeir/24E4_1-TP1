# Escreva um código usando list comprehension que retorne
# os caracteres individuais de uma string que não são caracteres de espaço em branco.
# Aplique-a à string "Sítio do pica-pau amarelo \n 2023”.

# Definindo a string
string = "Sítio do pica-pau amarelo \n 2023"

# Usando list comprehension
semEspacos = [char for char in string if char != ' ']

# Imprimindo a lista
print(semEspacos)
# Problema 1157 - Beecrowd - Iniciante - Nível 1

# Lendo o valor inteiro
entrada = int(input())
# Variável auxiliar
i = 1
# Loop para conferir divisores
while i <= entrada:
  # Teste de divisor e impressão em caso afirmativo
  if(entrada % i == 0):
    print(i)
  # Incrementando variável de controle do loop
  i += 1

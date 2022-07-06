# Função random é feito primeiro o import

import anotacoesrand
# irá gerar um número decimal aleatório, geralmente bem grande.

# exemplo
numero_random = random.random() * 10
# irá gerar um número aleatorio vezes 10

# convertendo para int, para mostrar apenas 2 casas decimais
int(numero_random)
# exemplo 10, 20,30 etc.

# a função round arredodanda o valor
# exemplo se for 4.5, irá ficar 5.
round(numero_random)

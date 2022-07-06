# Interpolação
print("Tentativa {} de {}" .format(3,10))
# Irá colocar o 3 no primeira CHAVE{} e o 10 na segunda CHAVE{}

"R$ {} .format (1.59)"
# Irá colocar o 1.59 dentro das CHAVES {}

# Para passarmos dentro do format o tipo float colocaremos assim.
"R$ {:f}.format(1.59)" # indicando dentro das chaves :f que é tipo float. R$ 1.590000

# Se quisermos colocar mais casas decimais
"R$ {:.2f}.format(1.59)"


# Com datas
"Data {:02d}/{:02d}".format(9,4)
# irá mostrar 09/04
# estamos colocando 02 dentro, e o d para especificar o tipo inteiro, e como queremos mostrar.
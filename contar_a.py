def contar_a(frase):
    contagem = frase.count("a")
    return contagem

frase = input("Digite uma frase: ")

resultado = contar_a(frase)
print(f"A letra 'a' aparece {resultado} vezes na frase")
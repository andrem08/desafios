def maiusculas(frase):
    frasefinal = ""
    for caractere in frase:
        if 65 <= ord(caractere) <= 90:
            frasefinal += caractere
    return frasefinal

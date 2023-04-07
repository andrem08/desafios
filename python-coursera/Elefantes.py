def incomodam(n):
    if n != int and n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n - 1)


def elefantes(n):
    #Caso base
    if not n > 1:
        return ''
    else:
        if n <= 2:
            return 'Um elefante incomoda muita gente' + '\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
        else:
            return elefantes(n - 1) + '\n' + str(n - 1) + ' elefantes incomodam muita gente' \
                + '\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'

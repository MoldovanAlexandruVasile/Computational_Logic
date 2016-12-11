'''

@author: Moldovan Alexandru-Vasile
Group: 915

'''


def multipluDoi(x):

    '''
    Tests if x it's a multiple of two
    :param x: The number which we are testing
    :return: True - if x it's multiple of two
             False - otherwise
    '''

    while x % 2 == 0: x = x // 2
    if x == 1: return True
    else: return False


def validBase(x):

    '''
    Tests if x is a number between 2 - 16
    :param x: The number wich we are testing
    :return: True - if x it's valid
             False - otherwise
    '''

    try:
        x = int(x)
        if x >= 2 and x <= 16: return True
        else: return False
    except ValueError: return False


def validMenuCommand(x):

    try:
        x = int(x)
        if x >= 0 and x <= 16 : return True
        else: return False
    except ValueError: return False
    

def readCommand():

    '''
    This function reads a number from the keyboard. The number it's the wanted command
    :return: cmd - An integer number
    '''

    sem = False
    while sem == False:
        cmd = input("\n Your command: ")
        if validMenuCommand(cmd) == True:
            sem = True
            return int(cmd)
        else: print("\n Invalid data !")


def readBase():

    '''
    Reads a number that must be between 2 and 16
    :return: True - if x it is
             False - otherwise
    '''

    sem = False
    while sem == False:
        x = input("\n \t Base: ")
        if validBase(x) == True:
            sem = True
            return int(x)
        else: print("\n Invalid data !")
        
    
def addition(a,b,c):
    '''
    This function adds two given numbers in a given base
    :param a: number 1
    :param b: number 2
    :param c: base
    :return: The sum
    '''

    x = a
    y = b
    base = c
    result = ''

    if len(x) < len(y):
            x,y = y,x
    lx = list(x)
    ly = list(y)

    dif = len(lx) - len(ly)
    i = 0
    while i < dif:
        ly.insert(0,'0')
        i = i + 1

    if base == 16:
        l = len(lx) - 1
        while l >= 0:
            if lx[l] == 'A' or lx[l] == 'a': lx[l] = '10'
            elif lx[l] == 'B' or lx[l] == 'b': lx[l] = '11'
            elif lx[l] == 'C' or lx[l] == 'c': lx[l] = '12'
            elif lx[l] == 'D' or lx[l] == 'd': lx[l] = '13'
            elif lx[l] == 'E' or lx[l] == 'e': lx[l] = '14'
            elif lx[l] == 'F' or lx[l] == 'f': lx[l] = '15'
                
            if ly[l] == 'A' or ly[l] == 'a': ly[l] = '10'
            elif ly[l] == 'B' or ly[l] == 'b': ly[l] = '11'
            elif ly[l] == 'C' or ly[l] == 'c': ly[l] = '12'
            elif ly[l] == 'D' or ly[l] == 'd': ly[l] = '13'
            elif ly[l] == 'E' or ly[l] == 'e': ly[l] = '14'
            elif ly[l] == 'F' or ly[l] == 'f': ly[l] = '15'
            l = l - 1
               
    r = list(result)
    i = 0 
    while i < len(lx):
        r.append('0')
        i = i + 1

    CF = 0
    l = len(lx) - 1
    while l >= 0:
        z = int(lx[l]) + int(ly[l]) + CF
        if z < base: CF = 0
        elif z == base:
            CF = 1
            z = 0 
        elif z > base:
            CF = 1
            z = z - base
        
        if z == 10: r[l] = "A"
        elif z == 11: r[l] = "B"
        elif z == 12: r[l] = "C"
        elif z == 13: r[l] = "D"
        elif z == 14: r[l] = "E"
        elif z == 15: r[l] = "F"
        else: r[l] = str(z)
        l = l - 1
        if l < 0 and CF == 1:
            r.insert(0,'1')
            
    for i in range(len(r)):
        result = result + str(r[i])

    return result
    

def subtraction(a,b,c):

    '''

    This function subtracts two given numbers in a given base
    :param a: number 1
    :param b: number 2
    :param c: base
    :return: The difference
    '''

    x = a
    y = b
    base = c
    result = ''

    if len(x) < len(y):
            x,y = y,x
    lx = list(x)
    ly = list(y)

    dif = len(lx) - len(ly)
    i = 0
    while i < dif:
        ly.insert(0,'0')
        i = i + 1

    if base == 16:
        l = len(lx) - 1
        while l >= 0:
            if lx[l] == 'A' or lx[l] == 'a': lx[l] = '10'
            elif lx[l] == 'B' or lx[l] == 'b': lx[l] = '11'
            elif lx[l] == 'C' or lx[l] == 'c': lx[l] = '12'
            elif lx[l] == 'D' or lx[l] == 'd': lx[l] = '13'
            elif lx[l] == 'E' or lx[l] == 'e': lx[l] = '14'
            elif lx[l] == 'F' or lx[l] == 'f': lx[l] = '15'
                
            if ly[l] == 'A' or ly[l] == 'a': ly[l] = '10'
            elif ly[l] == 'B' or ly[l] == 'b': ly[l] = '11'
            elif ly[l] == 'C' or ly[l] == 'c': ly[l] = '12'
            elif ly[l] == 'D' or ly[l] == 'd': ly[l] = '13'
            elif ly[l] == 'E' or ly[l] == 'e': ly[l] = '14'
            elif ly[l] == 'F' or ly[l] == 'f': ly[l] = '15'
            l = l - 1
                
    r = list(result)
    i = 0 
    while i < len(lx):
        r.append('0')
        i = i + 1

    l = len(lx) - 1
    CF = 0
    while l >= 0:
        if int(lx[l]) < int(ly[l]):
            if int(lx[l]) == 0 and CF == 0:
                lx[l] = str(base)
            CF = 1
            k = l - 1
            while int(lx[k]) == 0:
                lx[k] = str(base - 1)
                k = k - 1
            lx[k] = str(int(lx[k]) - 1)
        else: CF = 0

        z = CF * base + int(lx[l]) - int(ly[l])

        if z >= base: z = z - base

        if z == 10: r[l] = "A"
        elif z == 11: r[l] = "B"
        elif z == 12: r[l] = "C"
        elif z == 13: r[l] = "D"
        elif z == 14: r[l] = "E"
        elif z == 15: r[l] = "F"
        else: r[l] = str(z)

        l = l - 1
        
    i = 0
    while i < len(r):
        if r[i] == '0': del r[i]
        elif r[i] != '0': i = len(r)
        else: i = i + 1

    for i in range(len(r)):
        result = result + str(r[i])
            
    return result


def multiplication(a,b,c):

    '''
    This function multiplies two given numbers in a given base
    :param a: number 1
    :param b: number 2
    :param c: base
    :return: The multiplication
    '''

    x = a
    y = b
    base = c
    result = ''

    if len(x) < len(y):
            x,y = y,x
    lx = list(x)
    y = str(y)

    r = list(result)
    i = 0 
    while i < len(lx):
        r.append('0')
        i = i + 1
    
    if base == 16:
        l = len(lx) - 1
        while l >= 0:
            if lx[l] == 'A' or lx[l] == 'a': lx[l] = '10'
            elif lx[l] == 'B' or lx[l] == 'b': lx[l] = '11'
            elif lx[l] == 'C' or lx[l] == 'c': lx[l] = '12'
            elif lx[l] == 'D' or lx[l] == 'd': lx[l] = '13'
            elif lx[l] == 'E' or lx[l] == 'e': lx[l] = '14'
            elif lx[l] == 'F' or lx[l] == 'f': lx[l] = '15'

            if y == 'A' or y == 'a': y = '10'
            elif y == 'B' or y == 'b': y = '11'
            elif y == 'C' or y == 'c': y = '12'
            elif y == 'D' or y == 'd': y = '13'
            elif y == 'E' or y == 'e': y = '14'
            elif y == 'F' or y == 'f': y = '15'

            l = l - 1

    CF = 0
    l = len(lx) - 1
    while l >= 0:
        z = CF + (int(lx[l]) * int(y))
        CF = z // base
        modz = z % base
        if modz == 10: r[l] = "A"
        elif modz == 11: r[l] = "B"
        elif modz == 12: r[l] = "C"
        elif modz == 13: r[l] = "D"
        elif modz == 14: r[l] = "E"
        elif modz == 15: r[l] = "F"
        else: r[l] = modz

        l = l - 1

    if CF != 0: r.insert(0,str(CF))

    for i in range(len(r)):
        result = result + str(r[i])

    return result


def division(a,b,c):

    '''
    This function divide two given numbers in a given base
    :param a: number 1
    :param b: number 2
    :param c: base
    :return: The result
    '''

    x = str(a)
    y = str(b)
    base = c
    result = ''

    if len(x) < len(y):
        x,y = y,x

    lx = list(x)
    y = str(y)


    r = list(result)
    i = 0
    while i < len(lx):
        r.append('0')
        i = i + 1

    if base == 16:
        l = len(lx) - 1
        while l >= 0:
            if lx[l] == 'A' or lx[l] == 'a': lx[l] = '10'
            elif lx[l] == 'B' or lx[l] == 'b': lx[l] = '11'
            elif lx[l] == 'C' or lx[l] == 'c': lx[l] = '12'
            elif lx[l] == 'D' or lx[l] == 'd': lx[l] = '13'
            elif lx[l] == 'E' or lx[l] == 'e': lx[l] = '14'
            elif lx[l] == 'F' or lx[l] == 'f': lx[l] = '15'

            if y == 'A' or y == 'a': y = '10'
            elif y == 'B' or y == 'b': y = '11'
            elif y == 'C' or y == 'c': y = '12'
            elif y == 'D' or y == 'd': y = '13'
            elif y == 'E' or y == 'e': y = '14'
            elif y == 'F' or y == 'f': y = '15'

            l = l - 1

    divz = int(lx[0]) // int(y)
    modz = int(lx[0]) % int(y)
    if divz != 0: r[0] = str(divz)
    l = 1
    while l < len(x):
        CF = modz * base + int(lx[l])
        modz = CF % int(y)
        divz = CF // int(y)

        if divz == 10: r[l] = "A"
        elif divz == 11: r[l] = "B"
        elif divz == 12: r[l] = "C"
        elif divz == 13: r[l] = "D"
        elif divz == 14: r[l] = "E"
        elif divz == 15: r[l] = "F"
        else: r[l] = str(divz)

        l = l + 1

    i = 0
    while i < len(r):
        if r[i] == '0': del r[i]
        elif r[i] != '0': i = len(r)
        else: i = i + 1

    for i in range(len(r)):
        result = result + str(r[i])

    if modz == 10: modz = "A"
    elif modz == 11: modz = "B"
    elif modz == 12: modz = "C"
    elif modz == 13: modz = "D"
    elif modz == 14: modz = "E"
    elif modz == 15: modz = "F"

    return [result,modz]


def rapidConversion(a,x,y):

    '''
    This function converts a given number, from a given base, into another given base
    The bases must be multiple of two
    :param a: number
    :param x: convert from base
    :param y: converts into base
    :return: The converted number
    '''

    hexa = [['0', '0', '0', '0'], ['0', '0', '0', '1'], ['0', '0', '1', '0'], ['0', '0', '1', '1'], ['0', '1', '0', '0'], ['0', '1', '0', '1'], ['0', '1', '1', '0'],
            ['0', '1', '1', '1'], ['1', '0', '0', '0'], ['1', '0', '0', '1'], ['1', '0', '1', '0'], ['1', '0', '1', '1'], ['1', '1', '0', '0'], ['1', '1', '0', '1'],
            ['1', '1', '1', '0'], ['1', '1', '1', '1']]

    octa = [['0', '0', '0'], ['0', '0', '1'], ['0', '1', '0'], ['0', '1', '1'], ['1', '0', '0'], ['1', '0', '1'], ['1', '1', '0'],
            ['1', '1', '1'] ]

    quadra = [['0', '0'], ['0', '1'], ['1', '0'], ['1', '1']]

    binary = [['0'], ['1']]

    result = ''
    r = []

    b = x
    k1 = 0
    while b != 1:
        if b % 2 == 0:
            k1 += 1
            b = b // 2
    b = y
    k2 = 0
    while b != 1:
        if b % 2 == 0:
            k2 += 1
            b = b // 2

    if x == 16:
        l = len(a) - 1
        while l >= 0:
            if a[l] == 'A' or a[l] == 'a': a[l] = '10'
            elif a[l] == 'B' or a[l] == 'b': a[l] = '11'
            elif a[l] == 'C' or a[l] == 'c': a[l] = '12'
            elif a[l] == 'D' or a[l] == 'd': a[l] = '13'
            elif a[l] == 'E' or a[l] == 'e': a[l] = '14'
            elif a[l] == 'F' or a[l] == 'f': a[l] = '15'
            l = l - 1

    i = len(a) - 1
    while i >= 0:
        c = int(a[i])
        l = hexa[c][:]
        cate = len(l) - k1
        while cate != 0:
            del l[0]
            cate = cate - 1
        r.insert(0,l)
        i = i - 1

    for i in range(len(r)):
        l = r[i]
        for j in range(len(l)):
            result = result + str(l[j])

    r = result
    result = ''

    while len(r) % k2 != 0:
        r = '0' + r

    r = list(r)

    l2 = []
    i = 0
    while i < len(r) - 1:
        l = []
        j = i
        nr = 0
        while nr < k2:
            l.append(r[j])
            j = j + 1
            nr = nr + 1
        i = j
        l2.append(l)
    r = l2

    result = ''
    b = []
    i = 0
    if y == 2: b = binary
    elif y == 4: b = quadra
    elif y == 8: b = octa
    elif y == 16: b = hexa

    while i < len(r):

        j = 0
        while r[i] != b[j] and j < len(b) - 1: j = j + 1


        if j == 10: j = "A"
        elif j == 11: j = "B"
        elif j == 12: j = "C"
        elif j == 13: j = "D"
        elif j == 14: j = "E"
        elif j == 15: j = "F"
        else: j = str(j)

        result = result + j

        i = i + 1

    print("\n \t Result: ", result, " base ", y)


def succesiveDivisions(a,b,c):

    '''
    This function converts a given number, from a given base, into another given base
    The base from we converts must be smaller than the base we want to convert in
    :param a: number
    :param b: convert from base
    :param c: convert into base
    :return: The converted number
    '''

    rezfinal = ''
    k = 2
    mod = division(a, c, b)[1]
    result = division(a,c,b)[0]
    rezfinal = str(mod) + rezfinal

    while k > 1:
        mod = division(result, c, b)[1]
        result = division(result, c, b)[0]
        rezfinal = str(mod) + rezfinal
        try:
            if int(result) == 1 or int(result) == 0: k = 1
        except ValueError: pass
    mod = division(result, c, b)[1]
    rezfinal = str(mod) + rezfinal
    print("\n \t Result: ",rezfinal," base ", c)


def substitution(a,b,c):

    '''
    This function converts a given number, from a given base, into another given base
    The base from we converts must be greater than the base we want to convert in
    :param a: number
    :param b: convert from base
    :param c: convert into base
    :return: The converted number
    '''

    p = len(a) - 1
    k = 0
    result = '0'
    while k < len(a):
        inm = ''
        i = 1
        if p == 0: inm = a[len(a) - 1]
        elif p == 1: inm = multiplication(a[len(a) - 2], str(b), c)
        else:
            inm = multiplication(str(b), str(b), c)
            while i < p - 1:
                inm = multiplication(str(inm), str(b), c)
                i = i + 1
            inm = multiplication(str(inm), a[k], c)
        result = addition(result, str(inm), c)
        p = p - 1
        k = k + 1

    print("\n \t Result: ", result," base: ",c)

def conversion():

    '''
    This function calls the needed function for the conversion
    '''

    x = input("\n \t Number: ")
    lx = list(x)
    fromBase = readBase()
    print("\n \t Convert in")
    intoBase = readBase()

    if multipluDoi(fromBase) == True and multipluDoi(intoBase) == True: rapidConversion(lx, fromBase, intoBase)
    elif fromBase > intoBase: succesiveDivisions(x, fromBase,intoBase)
    elif fromBase < intoBase: substitution(lx, fromBase,intoBase)
    else: print("\n \t Invalid data !")

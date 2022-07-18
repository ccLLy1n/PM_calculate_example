import sys

def error_handler(equation, length):  
    a = length
    err_counter = 0

    for i in range (1, a, 2):
        asc = ord(equation[i])
        if asc < 41 or asc > 48 or asc == 44 or asc == 46:
            print ('invalid value!!!')
            err_counter += 1
            break

    for j in range (0, a, 2):
        num = ord(equation[j])
        if num < 48 and num > 57:
            print ('invalid value!!!')
            err_counter += 1
            break

    return err_counter

def plus(equation):
    Ans = int(equation[0]) + int(equation[2])
    return Ans

def minus(equation):
    Ans = int(equation[0]) - int(equation[2])
    return Ans

def multi(equation):
    Ans = int(equation[0]) * int(equation[2])
    return Ans

def divi(equation):
    Ans = int(equation[0]) / int(equation[2])
    return Ans

if __name__ == '__main__':
    equ = input("Please type something to culculate:")
    split = equ.split(" ")
    length = len(split)
    err_value = error_handler(split, length)
    e = split

    for i in range (1, length, 2):
        if e[i] == '+':
            result = plus(e)
        if e[i] == '-':
            result = minus(e)
        if e[i] == '*':
            result = multi(e)
        if e[i] == '/':
            result = int(divi(e))

    print(result)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import calcoohija


fd = open(sys.argv[1], 'r')
listalineas = fd.readlines()
fd.close()

suma = 0
resta = 0
multipli = 1
divi = 1

micalculadora = calcoohija.CalculadoraHija()

for lineas in range(0, len(listalineas)):
    linea = listalineas[lineas].split(',')
    if linea[0] == "suma":
        for numero in range(1, len(linea)):
            op1 = suma
            op2 = int(linea[numero])
            suma = micalculadora.plus(op1, op2)
        print(suma)
    if linea[0] == "resta":
        resta = int(linea[1])
        for numero in range(2, len(linea)):
            op1 = resta
            op2 = int(linea[numero])
            resta = micalculadora.minus(op1, op2)
        print(resta)
    if linea[0] == "multiplica":
        for numero in range(1, len(linea)):
            op1 = multipli
            op2 = int(linea[numero])
            multipli = micalculadora.multipliedby(op1, op2)
        print(multipli)
    if linea[0] == "divide":
        divi = int(linea[1])
        for numero in range(2, len(linea)):
            op1 = divi
            op2 = int(linea[numero])
            divi = micalculadora.dividedby(op1, op2)
        print(int(divi))

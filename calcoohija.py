#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

class Calculadora:
    def plus(self, op1, op2):
        return op1 + op2
		
    def minus(self, op1, op2):
        return op1 - op2
        
class CalculadoraHija(Calculadora):
    def multipliedby(self, op1, op2):
        return op1 * op2
        
    def dividedby(self, op1, op2):
        if op2 != 0:
            return op1 / op2
        else:
            print ["Division by zero is not allowed."]



if __name__ == "__main__":
	micalculadora=Calculadora()
	micalculadorahija=CalculadoraHija()
try:
    operando1 = int(sys.argv[1])
    operando2 = int(sys.argv[3])   
except ValueError:
    sys.exit("Error: Non numerical parameters")

if sys.argv[2] == "suma": 
	result = micalculadora.plus(operando1, operando2)
elif sys.argv[2] == "resta":
    result = micalculadora.minus(operando1, operando2)
elif sys.argv[2] == "multiplica":
    result = micalculadorahija.multipliedby(operando1, operando2)
elif sys.argv[2] == "divide":
    result = micalculadorahija.dividedby(operando1, operando2)
else:
    sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')
print(result)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import calcoo  #Utilizando el programa anterior, calcoo, no hace falta poner la suma ni la resta ya lo sabe el programa

class CalculadoraHija(calcoo.Calculadora):
    def multipliedby(self, op1, op2):
        return op1 * op2
        
    def dividedby(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed.")



if __name__ == "__main__":
	micalculadora = CalculadoraHija()
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
		result = micalculadora.multipliedby(operando1, operando2)
	elif sys.argv[2] == "divide":
		result = micalculadora.dividedby(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')
	print(result)

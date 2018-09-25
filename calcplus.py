#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 

fd = open(sys.argv[1], 'r')
listalineas = fd.readlines()
fd.close()
lineasseparadas=[]
suma=0
resta=0
multipli=1
divi=1
si=False
print(listalineas)
for lineas in range(0,len(listalineas)):
	linea=listalineas[lineas].split(',')
	
	if linea[0]=="suma":
		for numero in range(1,len(linea)):
			suma= int(linea[numero])+ suma
		print(suma)
	if linea[0]=="resta":
		resta=int(linea[1])
		for numero in range(2,len(linea)):
			resta=resta-int(linea[numero])
		print(resta)
	if linea[0]=="multiplica":
		for numero in range(1,len(linea)):
			multipli=multipli*int(linea[numero])
		print(multipli)
	if linea[0]=="divide":
		try:
			divi=int(linea[1])
			for numero in range(2,len(linea)):
				divi=divi/int(linea[numero])
			print(int(divi))
		except ZeroDivisionError:
		 sys.exit("Division by zero is not allowed.")

#Função que retorna valor em Celsius
def fahrenheit(T):
	return (9 / 5) * T + 32

#Função que retorna valor em Fahrenheit
def celsius(T):
	return (5 / 9) * T - 32

temps = [x for x in range(12,43,3)]
i = 0

print("\t***Conversor de temperaturas***")

opc = int(input("(1) C -> F\n(2) F -> C\n->"))

print("\nTemperaturas convertidas:\n")
	
if(opc == 1):
	tempsF = list(map(celsius, temps))
	for F in tempsF:
		print(temps[i], "C -> ",round(F, 2), "F")
		i += 1
						
elif(opc == 2):
	tempsC = list(map(fahrenheit, temps))
	for C in tempsC:	
		print(temps[i], "F -> ", round(C, 2), "C")
		i += 1	
else:
	print("\t***Caractere inválido!!!***")

		
				
						
														

				
								
from tkinter import *
from tkinter.ttk import *




root=Tk()

frame=Frame(root, width=400, height=400)
frame.pack()

varOpcion=StringVar()



def buttonCode():
    
	if varOpcion.get()==v[0]:

		etiq.config(text=" Frutas Ácidas(Citricos, naranja, limon, mandarina, pomelo, lima, tomate)\n Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n"
			" Ajos y cebollas\n Huevos", justify="left")

	elif varOpcion.get()==v[1]:
		
		etiq.config(text=" Frutas Ácidas(Citricos, naranja, limon, mandarina, pomelo, lima, tomate)\n Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n"
			" Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n"
			" Cereales(Arroz, trigo y derivados, pan)\n Huevos\n Leche(Entera, semidesnatada, desnatada)\n Quesos\n M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n"
			" M---Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			" M---Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)")
		

	elif varOpcion.get()==v[2]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n"
			"M---Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Ajos y cebollas\n Huevos\n M---Mantequilla(No margarina)\n")

	elif varOpcion.get()==v[3]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n M---Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n"
			"Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n"
			"M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n M---Mantequilla(No margarina)\n"
			"M---Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[4]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n"
			"Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n"
			"Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n"
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n M---Leche(Entera, semidesnatada, desnatada)\n M---Mantequilla(No margarina)\n M---Quesos\n")

	elif varOpcion.get()==v[5]:
		
		etiq.config(text="Cereales(Arroz, trigo y derivados, pan)\n Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n M---Leche(Entera, semidesnatada, desnatada)\n M---Mantequilla(No margarina)\n M---Quesos\n"
			"M---Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[6]:
		
		etiq.config(text="Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n"
			"Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n Mantequilla(No margarina)\n M---Quesos\n Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[7]:
		
		etiq.config(text="Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n"
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n Leche(Entera, semidesnatada, desnatada)\n Mantequilla(No margarina)\n Quesos\n")

	elif varOpcion.get()==v[8]:
		
		etiq.config(text="Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n "
			"Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n M---Mantequilla(No margarina)\n M---Quesos\n"
			"Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[9]:
		
		etiq.config(text="Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n"
			"Cereales(Arroz, trigo y derivados, pan)\n Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[10]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n"
			"Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n Cereales(Arroz, trigo y derivados, pan)\n"
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n Huevos\n M---Leche(Entera, semidesnatada, desnatada)\n Mantequilla(No margarina)\n"
			"M---Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")

	elif varOpcion.get()==v[11]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n M---Cereales(Arroz, trigo y derivados, pan)\n "
			"M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n M---Huevos\n Leche(Entera, semidesnatada, desnatada)\n Mantequilla(No margarina)\n"
			"M---Quesos\n")

	elif varOpcion.get()==v[12]:
		
		etiq.config(text=" M---Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)\n M---Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n"
			"M---Cereales(Arroz, trigo y derivados, pan)\n M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n"
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"M---Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n Huevos\n"
			"Leche(Entera, semidesnatada, desnatada)\n Mantequilla(No margarina)\n M---Quesos\n")

	elif varOpcion.get()==v[13]:
		
		etiq.config(text="Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)\n M---Cereales(Arroz, trigo y derivados, pan)\n"
			"M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n"
			"M---Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)\n"
			"M---Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"M---Leche(Entera, semidesnatada, desnatada)\n M---Mantequilla(No margarina)\n Quesos\n")

	elif varOpcion.get()==v[14]:
		
		etiq.config(text="M---Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)\n"
			"M---Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)\n "
			"Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)\n"
			"Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)\n"
			"Ajos y cebollas\n M---Huevos\n Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)\n")
	


buttonSend=Button(frame, text="OK", command=buttonCode)
buttonSend.grid(row=2)

textInicial=Label(frame, text="Plan de Alimentos:")
textInicial.grid(row=0, sticky="nsew")



v=["1)-Frutas Ácidas(Citricos, naranja, limon, mandarina, pomelo, lima, tomate)", "2)-Frutas Semiácidas(Albaricoque, cereza, fresa, higo, kiwi, melocoton, piña, sandia, uva, manzana, pera)",
"3)-Frutas Dulces(ciruela, pasa, dátil, hogo seco, uva pasa)", "4)-Frutos oleaginosos(Aceite, aceituna, aguacate, almendra, coco, mantequilla de maní, nuez, pistacho, sésamo)", "5)-Cereales(Arroz, trigo y derivados, pan)",
"6)-Legumbres y geminados(Garbanzo, guisante, judía, lenteja, soja, cacahuete)", "7)-Hortalizas(Alcachofa, berenjena, calabaza, calabacin, judia tierna, nabo, pepino, pimiento, puerro, rábano, remolacha, zanahoria)",
"8)-Feculosas(Boniato, castaña, patata, plátano, zanahoria cocida)", "9)-Verduras y algas(Acelga, apio, berro, brócoli, coles, coliflor, escarola, espárragos, espinaca, lechuga, champiñones, setas)",
"10)-Ajos y cebollas", "11)-Huevos", "12)-Leche(Entera, semidesnatada, desnatada)", "13)-Mantequilla(No margarina)", "14)-Quesos", "15)-Carnes y pescados(Carnes, pescados y mariscos.Embutidos, conservas)"]



combo=Combobox(frame, values=v, textvariable=varOpcion, width=100)
combo.grid(row=1)
combo.set("Select")



etiq=Label(root)
etiq.pack()

root.mainloop()
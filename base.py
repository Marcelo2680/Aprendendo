#============ Bibliotecas ============#
from tkinter import *
from tkinter import font
import os
from PIL import Image, ImageTk
import numpy as np

#--------------------------------------

#=============Variáveis Importantes==============#


#-------------------------------------------------


#============== Funções ==============#
#Bloco 1
def bloco1():
    global imagem_rs_1, imagem_rs_2
    #Contorno Preto
    c1 = Label(ini, text = '', background = '#000000', foreground = '#FFFFFF', anchor = W)
    c1.place(x = 16, y = 16, width = 410, height = 260)

    #Quadro Principal 1
    q1 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q1.place(x = 20, y = 20, width = 400, height = 250)

    #Topo do Quadro 1
    tp1 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W)
    tp1.place(x = 20, y = 20, width = 400, height = 40)

    #Título do Bloco 1
    Label(ini, text = 'Associação de Resistores', font = fonte17, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 85, y = 23, width = 300, height = 30)

    #Texto 1
    Label(ini, text = 'Escolha como quer associar os Resistores', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 33, y = 70, width = 385, height = 20)

    #Botões para selscionar serie ou paralelo
    Button(ini, text = 'Série', font = fonte14, command = r_serie, background = '#FFFFFF', foreground = '#343541').place(x = 75, y = 100, width = 100, height = 30)
    Button(ini, text = 'Paralelo', font = fonte14, command = r_paralelo, background = '#FFFFFF', foreground = '#343541').place(x = 265, y = 100, width = 100, height = 30)

    #Obtendo endereço do arquivo
    diretorio_script = os.path.dirname(__file__)

    #Manipulando as Imagem
    caminho_imagem1 = os.path.join(diretorio_script, "Imagens\serie_resistor.png")
    imagem1 = Image.open(caminho_imagem1)
    imagem_rs_1 = ImageTk.PhotoImage(imagem1)
    Label(ini, image=imagem_rs_1).place(x = 37, y = 140)


    caminho_imagem2 = os.path.join(diretorio_script, "Imagens\paralelo_resistor.png")
    imagem2 = Image.open(caminho_imagem2)
    imagem_rs_2 = ImageTk.PhotoImage(imagem2)
    Label(ini, image=imagem_rs_2).place(x = 225, y = 140)

#Bloco 2
def bloco2():
    #Contorno Preto
    c2 = Label(ini, text = '', background = '#000000', foreground = '#FFFFFF', anchor = W)
    c2.place(x = 16, y = 282, width = 218, height = 260)

    #Quadro Principal 2
    q2 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q2.place(x = 20, y = 286, width = 210, height = 250)

    #Topo do Quadro 2
    tp2 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W) 
    tp2.place(x = 20, y = 286, width = 210, height = 40)

    #Título do Bloco 2
    Label(ini, text = 'Lei de Ohm', font = fonte17, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 60, y = 295, width = 120, height = 20)

    #Checkbox para ver configurações dos resistores
    def checkbox_corrente():
        I==True

    def checkbox_tensao():
        V==True

    def checkbox_resistencia():
        R==True

    #Definindo variaveis de controle das checkboxs   
    V = BooleanVar()
    R = BooleanVar()
    I = BooleanVar()


    Label(ini, text='Marque e Insira os valores', font = fonte11, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=30, y=330, width=180, height=25)
    Label(ini, text='que você sabe:', font = fonte11, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=30, y=355, width=100, height=20)

    #Checkboxs
    Checkbutton(ini, text="", variable=I, command=checkbox_corrente, background = '#525253',foreground = '#000000', anchor = W).place(x=25, y=390, width=100, height=25)
    Label(ini, text='I =', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=55, y=390, width=100, height=25)
    Checkbutton(ini, text="", variable=V, command=checkbox_corrente, background = '#525253',foreground = '#000000', anchor = W).place(x=25, y=420, width=100, height=25)
    Label(ini, text='V =', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=50, y=420, width=100, height=25)
    Checkbutton(ini, text="", variable=R, command=checkbox_corrente, background = '#525253',foreground = '#000000', anchor = W).place(x=25, y=450, width=100, height=25)
    Label(ini, text='R =', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=50, y=450, width=100, height=25)

    i = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    i.place(x=90, y=390, width=40, height=25)
    Label(ini, text='Ampéres', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=135, y=390, width=85, height=25)

    v = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    v.place(x=90, y=420, width=40, height=25)
    Label(ini, text='Volts', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=135, y=420, width=80, height=25)

    r = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    r.place(x=90, y=450, width=40, height=25)
    Label(ini, text='Ohms', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=135, y=450, width=80, height=25)

    def leideohm():
        ohms = '\u03A9'
        if R.get() == False:
            volts = float(v.get())
            corrente = float(i.get())
            resistencia=volts/corrente
            Label(ini, text='R={:.4e}{}'.format(resistencia,ohms), font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 85, y = 490, width = 140, height = 30)
            
        elif V.get() == False:
            corrente = float(i.get())
            resistencia = float(r.get())
            volts = corrente*resistencia
            Label(ini, text='V = {:.4e} V'.format(volts), font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 85, y = 490, width = 145, height = 30)
            
        elif I.get() == False:
            volts = float(v.get())        
            resistencia = float(r.get())
            corrente = volts/resistencia
            Label(ini, text='I = {:.4e} A'.format(corrente), font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 85, y = 490, width = 140, height = 30)
            

    Button(ini, text = 'Calcular', font = fonte10, command = leideohm, background = '#FFFFFF', foreground = '#343541').place(x = 25, y = 490, width = 60, height = 30)

#Bloco 3
def bloco3():
    #Contorno Preto
    c3 = Label(ini, text = '', background = '#000000', foreground = '#FFFFFF', anchor = W)
    c3.place(x = 246, y = 282, width = 535, height = 260)

    #Quadro Principal 3
    q3 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q3.place(x = 250, y = 286, width = 525, height = 250)

    #Topo do Quadro 3
    tp3 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W) 
    tp3.place(x = 250, y = 286, width = 525, height = 40)

    #Título do Bloco 3
    Label(ini, text = 'Conversão de Energia', font = fonte17, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 390, y =290, width = 250, height = 30)

    Button(ini, text = 'NI = Hclc + Hglg', font = fonte14, command = leideampere, background = '#FFFFFF', foreground = '#343541').place(x = 275, y = 340, width = 150, height = 30)
    Button(ini, text = 'Indutância', font = fonte14, command = indutância_conv, background = '#FFFFFF', foreground = '#343541').place(x = 435, y = 340, width = 150, height = 30)
    Button(ini, text = 'B = uH', font = fonte14, command = bh, background = '#FFFFFF', foreground = '#343541').place(x = 595, y = 340, width = 150, height = 30)
    Button(ini, text = 'Relutância', font = fonte14, command = relut, background = '#FFFFFF', foreground = '#343541').place(x = 275, y = 380, width = 150, height = 30)
    Button(ini, text = 'Formulário', font = fonte14, command = formulas, background = '#FFFFFF', foreground = '#343541').place(x = 275, y = 490, width = 150, height = 30)

#Bloco 4
def bloco4():
    global imagem_rs_4
    #Contorno Preto
    c4 = Label(ini, text = '', background = '#000000', foreground = '#FFFFFF', anchor = W)
    c4.place(x = 436, y = 16, width = 325, height = 260)

    #Quadro Principal 3
    q4 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q4.place(x = 440, y = 20, width = 315, height = 250)

    #Topo do Quadro 3
    tp4 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W) 
    tp4.place(x = 440, y = 20, width = 315, height = 40)

    #Título do Bloco 3
    Label(ini, text = 'Divisor de Tensão', font = fonte17, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 500, y = 25, width = 250, height = 30)

    #Obtendo endereço do arquivo
    diretorio_script = os.path.dirname(__file__)

    #Manipulando as Imagem
    caminho_imagem4 = os.path.join(diretorio_script, "Imagens\divisorv.png")
    imagem4 = Image.open(caminho_imagem4)
    imagem_rs_4 = ImageTk.PhotoImage(imagem4)
    Label(ini, image=imagem_rs_4).place(x = 495, y = 65, width = 300, height = 280)




#Resistores em Série
def r_serie():
    #Quadro Principal 1
    q1 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q1.place(x = 20, y = 60, width = 400, height = 210)

    #Topo do Quadro 1
    tp1 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W)
    tp1.place(x = 20, y = 20, width = 350, height = 40)

    #Título do Bloco 1
    Label(ini, text = 'Resistores em Série', font = fonte17, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 115, y = 28, width = 300, height = 20)

    #Botão de voltar
    def voltar():
        bloco1()
        
    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    #Manipulando as Imagem
    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image = imagem_vlt,  command = voltar).place(x = 395, y = 30, width = 20, height = 20)
    global n
    #Entrando com valores de resistencia
    Label(ini, text = ' ', background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=60, y=95, width=80, height=45)
    Label(ini, text = 'Quantos Resistores você deseja associar?', font = fonte14, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 33, y = 70, width = 385, height = 20)
    n = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    n.place(x=65, y=100, width=70, height=35)

    #Checkbox para ver configurações dos resistores

    def checkbox_clickmv():
        v1 = True
        v2.set(False)
        Button(ini, text = 'Calcular', font = fonte15, command = calcular, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)

    def checkbox_clickvd():
        v2 = True
        v1.set(False)
    
    global v1,v2
    #Definindo variaveis de controle das checkboxs   
    v1 = BooleanVar()
    v2 = BooleanVar()
    
    #Checkboxs
    mv = Checkbutton(ini, text="", variable=v1, command=checkbox_clickmv, background = '#525253',foreground = '#000000', anchor = W).place(x=145, y=95, width=250, height=25)
    Label(ini, text='Todos os valores de Resistência são iguais', background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=165, y=95, width=250, height=25)
    vd = Checkbutton(ini, text="", variable=v2, command=checkbox_clickvd, background = '#525253',foreground = '#000000', anchor = W).place(x=145, y=115, width=270, height=25)
    Label(ini, text='Nem todos os valores de Resistência são iguais', background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=165, y=115, width=250, height=25)

    #Solicitação dos valores dos resistores iguais
    Label(ini, text='Valor dos Resistores:', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=33, y=145, width=250, height=25)    
    Label(ini, text = ' ', background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=233, y=140, width=125, height=35)
    Label(ini, text='Ohms', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=360, y=145, width=56, height=25)    
    valor = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    valor.place(x=238, y=145, width=115, height=25)
    global g
    g = 1 
   
   #função para calcular a Req
    def calcular():
        global g
        #Valores Iguais de Resistores
        if v1.get()==True:
            g = 1
            #calculo de Req
            num_res = int(n.get())
            val_res = float(valor.get())
            req_serie = num_res*val_res
            #Mostra na tela o valor de Req
            Label(ini, text=' ', background = '#000000').place(x=32, y=222, width=380, height=40)    
            Label(ini, text=' Resistência Equivalente:', font = fonte12, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=38, y=227, width=300, height=30)    
            if req_serie < 1:
                Label(ini, text='{:.4e} Ohms'.format(req_serie), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  
            else:
                Label(ini, text='{:.4f} Ohms'.format(req_serie), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  
        #Valores diferentes de resistores
        if v2.get()==True: 
            if g == 0:
                #salvamento de dados em dicionario utilizando Entry 
                valores_resistores = []
                val_res = 0
                val_res = float(valor.get())
                for entry in entries_resistores:
                    valor_resistor = entry.get()
                    valores_resistores.append(float(valor_resistor))
                #calculo de Req
                req_serie1 = sum(valores_resistores)
                #Mostra na tela o valor de Req
                Label(ini, text=' ', background = '#000000').place(x=32, y=222, width=380, height=40)    
                Label(ini, text=' Resistência Equivalente:', font = fonte12, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=38, y=227, width=300, height=30)    
                if req_serie1 < 1:
                    Label(ini, text='{:.4e} Ohms'.format(req_serie1), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  
                else:
                    Label(ini, text='{:.4f} Ohms'.format(req_serie1), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  

    def valores_diferentes():
        if v2.get() == True:
            global g
            g = 0
            global n
            num_res = int(n.get())
            if num_res > 9:
                print('')
            elif num_res < 9:
                print(n.get())
                global entries_resistores
                global quadro_auxiliar
                global inserir_resis
                global entry
                entries_resistores = []
                i = 1
                quadro_auxiliar = Label(ini, text=" ", font=fonte14, background='#000000', foreground='#343541')
                quadro_auxiliar.place(x=420, y=20, width=110, height=250)
                while i <= num_res:
                    inserir_resis = Label(ini, text="R{} = ".format(i), font=fonte11, background='#000000', foreground='#FFFFFF')
                    inserir_resis.place(x=435, y=29 * i, width=40, height=25)
                    entry = Entry(ini, font=fonte14, background='#FFFFFF', foreground='#343541')
                    entry.place(x=473, y=29 * i, width=45, height=25)

                    entries_resistores.append(entry)
                    i = i + 1

                    

            #Button(ini, text = 'Calcular', font = fonte15, command = calcular1, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)
            
    
            #quando vc parou vc estava pensando em uma soluçao para associar resistores diferente 
            #e depois conseguir resistores iguais novamente e 



    Button(ini, text = 'Calcular', font = fonte15, command = calcular, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)
    Button(ini, text = 'Valores Diferentes', font = fonte15, command = valores_diferentes, background = '#FFFFFF', foreground = '#343541').place(x = 228, y = 180, width = 178, height = 30)

#Resistores em Pralelo
def r_paralelo():
    #Quadro Principal 1
    q1 = Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W)
    q1.place(x = 20, y = 60, width = 400, height = 210)

    #Topo do Quadro 1
    tp1 = Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W)
    tp1.place(x = 20, y = 20, width = 350, height = 40)

    #Título do Bloco 1
    Label(ini, text = 'Resistores em Paralelo', font = fonte17, background = '#0a0a41', foreground = '#FFFFFF', anchor = W).place(x = 100, y = 28, width = 300, height = 20)
    
    #Botão de voltar
    def voltar():
        bloco1()
    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    #Manipulando as Imagem
    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image = imagem_vlt,  command = voltar).place(x = 395, y = 30, width = 20, height = 20)


    #Entrando com valores de resistencia
    Label(ini, text = ' ', background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=60, y=95, width=80, height=45)
    Label(ini, text = 'Quantos Resistores você deseja associar?', font = fonte14, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 33, y = 70, width = 385, height = 20)
    n = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    n.place(x=65, y=100, width=70, height=35)

    #Checkbox para ver configurações dos resistores

    def checkbox_clickmv():
        v1 = True
        v2.set(False)
        Button(ini, text = 'Calcular', font = fonte15, command = calcular, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)

    def checkbox_clickvd():
        v2 = True
        v1.set(False)
        

    v1 = BooleanVar()
    v2 = BooleanVar()
    

    mv = Checkbutton(ini, text="", variable=v1, command=checkbox_clickmv, background = '#525253',foreground = '#000000', anchor = W).place(x=145, y=95, width=250, height=25)
    Label(ini, text='Todos os valores de Resistência são iguais', background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=165, y=95, width=250, height=25)
    vd = Checkbutton(ini, text="", variable=v2, command=checkbox_clickvd, background = '#525253',foreground = '#000000', anchor = W).place(x=145, y=115, width=270, height=25)
    Label(ini, text='Nem todos os valores de Resistência são iguais', background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=165, y=115, width=250, height=25)

    
    Label(ini, text='Valor dos Resistores:', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=33, y=145, width=250, height=25)    
    Label(ini, text = ' ', background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=233, y=140, width=125, height=35)
    Label(ini, text='Ohms', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=360, y=145, width=56, height=25)    
    valor = Entry(ini, font = fonte14, background='#FFFFFF', foreground='#343541')
    valor.place(x=238, y=145, width=115, height=25)

    g = 1 
   
    def calcular():
        global g
        print(valor.get())
        
        if v1.get()==True:
            g = 1
            
            print(valor.get())
            
            num_res = int(n.get())
            val_res = float(valor.get())
            req_serie = val_res/num_res
            
            
            Label(ini, text=' ', background = '#000000').place(x=32, y=222, width=380, height=40)    
            Label(ini, text=' Resistência Equivalente:', font = fonte12, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=38, y=227, width=300, height=30)    
            if req_serie < 1:
                Label(ini, text='{:.4e} Ohms'.format(req_serie), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  
            else:
                Label(ini, text='{:.4f} Ohms'.format(req_serie), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=220, y=227, width=185, height=30)  
        if v2.get() == True:
            if g == 0:
                valores_resistores = []
                for entry in entries_resistores:
                    valor_resistor = entry.get()
                    valores_resistores.append(float(valor_resistor))

                req_paralelo = 1 / sum(1 / valor for valor in valores_resistores)
                
                Label(ini, text=' ', background='#000000').place(x=32, y=222, width=380, height=40)
                Label(ini, text='Resistência Equivalente:', font=fonte12, background='#525253', foreground='#FFFFFF', anchor=W).place(x=38, y=227, width=300, height=30)
                if req_paralelo < 1:
                    Label(ini, text='{:.4e} Ohms'.format(req_paralelo), font=fonte13, background='#525253', foreground='#FFFFFF', anchor=W).place(x=220, y=227, width=185, height=30)
                else:
                    Label(ini, text='{:.4f} Ohms'.format(req_paralelo), font=fonte13, background='#525253', foreground='#FFFFFF', anchor=W).place(x=220, y=227, width=185, height=30)

    def valores_diferentes():
        if v2.get() == True:
            global g
            g = 0
            num_res = int(n.get())
            if num_res > 9:
                print('')
            elif num_res < 9:
                print(n.get())
                global entries_resistores
                entries_resistores = []
                i = 1
                Label(ini, text=" ", font=fonte14, background='#000000', foreground='#343541').place(x=420, y=20, width=110, height=250)
                while i <= num_res:
                    Label(ini, text="R{} = ".format(i), font=fonte11, background='#000000', foreground='#FFFFFF').place(
                        x=435, y=29 * i, width=40, height=25)

                    entry = Entry(ini, font=fonte14, background='#FFFFFF', foreground='#343541')
                    entry.place(x=473, y=29 * i, width=45, height=25)

                    entries_resistores.append(entry)
                    i = i + 1

                    

            #Button(ini, text = 'Calcular', font = fonte15, command = calcular1, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)
            
    
            #quando vc parou vc estava pensando em uma soluçao para associar resistores diferente 
            #e depois conseguir resistores iguais novamente e 



    Button(ini, text = 'Calcular', font = fonte15, command = calcular, background = '#FFFFFF', foreground = '#343541').place(x = 40, y = 180, width = 178, height = 30)
    Button(ini, text = 'Valores Diferentes', font = fonte15, command = valores_diferentes, background = '#FFFFFF', foreground = '#343541').place(x = 228, y = 180, width = 178, height = 30)

#Lei de Ampère
def leideampere():
    Label(ini, text='', background='#525253', foreground='#FFFFFF', anchor=W).place(x=250, y=326, width=525, height=210)
    Label(ini, text='', background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=250, y=286, width=525, height=40)
    Label(ini, text='Conversão de Energia', font=fonte10, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(
        x=610, y=293, width=140, height=25)
    Label(ini, text='Lei de Ampère', font=fonte20, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=300,
                                                                                                             y=290,
                                                                                                             width=200,
                                                                                                             height=35)

    # Botão de voltar
    def voltar3():
        bloco3()

    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image=imagem_vlt, command=voltar3).place(x=745, y=295, width=20, height=20)

    # Enunciado
    Label(ini, text='Clique nas variáveis que você já sabe:', font=fonte15, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=350, y=330, width=350, height=30)

    # INSERINDO AS VARIÁVEIS
    def checkbox_N():
        nes == True

    def checkbox_Hc():
        hc==True

    def checkbox_lc():
        lc==True

    def checkbox_I():
        amp==True

    def checkbox_Hg():
        hg==True

    def checkbox_lg():
        lg==True

    nes = BooleanVar()
    hc = BooleanVar()
    lc = BooleanVar()
    amp = BooleanVar()
    hg = BooleanVar()
    lg = BooleanVar()

    Checkbutton(ini, text="", variable=nes, command=checkbox_N, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=355, width=25, height=25)
    Label(ini, text='Número de Espiras (N)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=355, width=170, height=25)
    num_esp = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    num_esp.place(x=485, y=358, width=50, height=20)

    Checkbutton(ini, text="", variable=hc, command=checkbox_Hc, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=385, width=25, height=25)
    Label(ini, text='Campo no Núcleo (Hc)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=385, width=185, height=25)
    camp_c = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    camp_c.place(x=485, y=388, width=50, height=20)

    Checkbutton(ini, text="", variable=lc, command=checkbox_lc, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=415, width=25, height=25)
    Label(ini, text='Comprimento do núcleo (lc)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=415, width=205, height=25)
    comp_c = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    comp_c.place(x=485, y=418, width=50, height=20)

    Checkbutton(ini, text="", variable=amp, command=checkbox_I, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=445, width=25, height=25)
    Label(ini, text='Corrente (I)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=445, width=150, height=25)
    corr = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    corr.place(x=485, y=448, width=50, height=20)

    Checkbutton(ini, text="", variable=hg, command=checkbox_Hg, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=475, width=25, height=25)
    Label(ini, text='Campo no Gap (Hc)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=475, width=150, height=25)
    camp_g = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    camp_g.place(x=485, y=478, width=50, height=20)

    Checkbutton(ini, text="", variable=lg, command=checkbox_lg, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=505, width=25, height=25)
    Label(ini, text='Comprimento do Gap (lg)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=505, width=190, height=25)
    comp_g = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    comp_g.place(x=485, y=508, width=50, height=20)

    
    # Calculando
    def calcular4():
        e=0
        def erro():
            erro_window = Tk()
            erro_window.title('ERRO')
            erro_window.geometry('470x50')
            erro_window.configure(background='#FFFFFF')
            Label(erro_window, text='Não é possível calcular a LEI DE AMPERE utilizando apenas essas variáveis!',
                  background='#FFFFFF', foreground='#000000', anchor=W).place(x=35, y=10, width=500, height=25)
            erro_window.mainloop()

        if lg.get() and hc.get() and lc.get() and amp.get() and hg.get():
            campc = float(camp_c.get())
            compc = float(comp_c.get())
            corrent = float(corr.get())
            campg = float(camp_g.get())
            compg = float(comp_g.get())
            resp = ((campg * compg) + (campc * compc)) / corrent
            
            e=e + 1
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='N = {:.4e} Espiras'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
        
        if lg.get() and hc.get() and lc.get() and hg.get() and nes.get():
            numes = float(num_esp.get())
            campc = float(camp_c.get())
            compc = float(comp_c.get())
            campg = float(camp_g.get())
            compg = float(comp_g.get())
            resp = ((campg * compg) + (campc * compc)) / numes
            
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='I = {:.4e}A'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
            e=e + 1

        if lg.get() and hc.get() and lc.get() and amp.get() and nes.get():
            numes = float(num_esp.get())
            campc = float(camp_c.get())
            compc = float(comp_c.get())
            corrent = float(corr.get())
            compg = float(comp_g.get())
            resp = ((numes * corrent) - (campc * compc)) / compg
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='Hg = {:.4e}Ae/m'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
            e=e + 1

        if hc.get() and lc.get() and amp.get() and hg.get() and nes.get():
            numes = float(num_esp.get())
            campc = float(camp_c.get())
            corrent = float(corr.get())
            campg = float(camp_g.get())
            compc = float(comp_c.get())
            resp = ((numes * corrent) - (campc * compc)) / campg
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='lg = {:.4e}m'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
            e=e + 1

        if lg.get() and lc.get() and amp.get() and hg.get() and nes.get():
            numes = float(num_esp.get())
            compc = float(comp_c.get())
            corrent = float(corr.get())
            campg = float(camp_g.get())
            compg = float(comp_g.get())
            resp = ((numes * corrent) - (campg * compg)) / compc
            
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='Hc = {:.4e}Ae/m'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
            e=e + 1

        if lg.get() and hc.get() and amp.get() and hg.get() and nes.get():
            numes = float(num_esp.get())
            campc = float(camp_c.get())
            corrent = float(corr.get())
            campg = float(camp_g.get())
            compg = float(comp_g.get())
            resp = ((numes * corrent) - (campg * compg)) / campc
            
            Label(ini, text='', font=fonte13, background='#000000', foreground='#FFFFFF', anchor=W).place(x=550, y=400, width=215, height=50)
            Label(ini, text='lc = {:.4e}m'.format(resp), font=fonte13, background='#525253', foreground='#FFFFFF',
                  anchor=W).place(x=555, y=405, width=205, height=40)
            e=e + 1

        if e==0:
            erro()

    Button(ini, text='Calcular', font=fonte14, command=calcular4, background='#FFFFFF', foreground='#343541').place(
        x=670, y=500, width=100, height=30)

#Indutância em Conversão de Energia
def indutância_conv():
    Label(ini, text = '', background = '#525253', foreground = '#FFFFFF', anchor = W).place(x = 250, y = 326, width = 525, height = 210)
    Label(ini, text = '', background = '#0a0a41', foreground = '#FFFFFF', anchor = W) .place(x = 250, y = 286, width = 525, height = 40)
    Label(ini, text = 'Conversão de Energia', font = fonte10, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 610, y =293, width = 140, height = 25)
    Label(ini, text = 'INDUTÂNCIA', font = fonte20, background = '#0a0a41',foreground = '#FFFFFF', anchor = W).place(x = 300, y =290, width = 200, height = 35)

    #Botão de voltar
    def voltar3():
        bloco3()
        
    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image = imagem_vlt,  command = voltar3).place(x = 745, y = 295, width = 20, height = 20)

    #Enunciado
    Label(ini, text = 'Clique nas variáveis que você já sabe:', font = fonte15, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x = 350, y =330, width = 350, height = 30)


    #INSERINDO AS VARIAVEIS
    def checkbox_N():
        ne == True

    def checkbox_B():
        b == True

    def checkbox_A():
        a == True
    
    def checkbox_I():
        i == True
    
    def checkbox_H():
        h == True

    def checkbox_l():
        l == True

    def checkbox_R():
        r == True

    def checkbox_u():
        u == True

    ne = BooleanVar()
    b = BooleanVar()
    a = BooleanVar()
    i = BooleanVar()
    h = BooleanVar()
    l = BooleanVar()
    r = BooleanVar()
    u = BooleanVar()

    Checkbutton(ini, text="", variable=ne, command=checkbox_N, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=355, width=25, height=25)
    Label(ini, text='Número de Espiras', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=355, width=150, height=25)
    num_esp = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    num_esp.place(x=445, y=358, width=50, height=20)

    Checkbutton(ini, text="", variable=b, command=checkbox_B, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=385, width=25, height=25)
    Label(ini, text='Densidade de Campo', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=385, width=165, height=25)
    dens_camp = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    dens_camp.place(x=445, y=388, width=50, height=20)

    Checkbutton(ini, text="", variable=a, command=checkbox_A, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=415, width=25, height=25)
    Label(ini, text='Área', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=415, width=150, height=25)
    area = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    area.place(x=445, y=418, width=50, height=20)

    Checkbutton(ini, text="", variable=i, command=checkbox_I, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=445, width=25, height=25)
    Label(ini, text='Corrente', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=445, width=150, height=25)
    corren = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    corren.place(x=445, y=448, width=50, height=20)

    Checkbutton(ini, text="", variable=h, command=checkbox_H, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=475, width=25, height=25)
    Label(ini, text='Campo Magnético', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=475, width=150, height=25)
    campo = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    campo.place(x=445, y=478, width=50, height=20)

    Checkbutton(ini, text="", variable=l, command=checkbox_l, background = '#525253',foreground = '#000000', anchor = W).place(x=255, y=505, width=25, height=25)
    Label(ini, text='Campo Magnético', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=505, width=150, height=25)
    comp = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    comp.place(x=445, y=508, width=50, height=20)

    Checkbutton(ini, text="", variable=r, command=checkbox_R, background = '#525253',foreground = '#000000', anchor = W).place(x=500, y=355, width=25, height=25)
    Label(ini, text='Relutância', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=525, y=355, width=150, height=25)
    relut = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    relut.place(x=615, y=358, width=50, height=20)

    Checkbutton(ini, text="", variable=u, command=checkbox_u, background = '#525253',foreground = '#000000', anchor = W).place(x=500, y=385, width=25, height=25)
    Label(ini, text='mi', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=525, y=385, width=165, height=25)
    mi = Entry(ini, font = fonte12, background='#FFFFFF', foreground='#343541')
    mi.place(x=615, y=388, width=50, height=20)


    #Calculando
    def calcular3():
        error = 0
        
        def erro():
            erro_window = Tk()
            erro_window.title('ERRO')
            erro_window.geometry('470x50')  # Aumentei o tamanho da janela de erro
            erro_window.configure(background='#FFFFFF')
            Label(erro_window, text='Não é possível calcular a INDUTÂNCIA utilizando apenas essas variáveis!', background = '#FFFFFF',foreground = '#000000', anchor = W).place(x=35, y=10, width=500, height=25)
            erro_window.mainloop()

        if ne.get() and b.get() and a.get() and i.get():      
            numesp = float(num_esp.get())
            denscamp = float(dens_camp.get())
            ar = float(area.get())
            corrente = float(corren.get())
            ind=(numesp*denscamp*ar)/corrente

            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=530, y=420, width=215, height=50)
            Label(ini, text='Indutância = {:.4e}H'.format(ind), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=535, y=425, width=205, height=40)
        elif error == 0:
            erro()
            error = error + 1

        if  ne.get() and r.get():
            numesp = float(num_esp.get())
            relutancia = float(relut.get())
            ind = (numesp**2)/relutancia
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=530, y=420, width=215, height=50)
            Label(ini, text='Indutância = {:.4e}H'.format(ind), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=535, y=425, width=205, height=40)
        elif error == 0:
            erro()
            error = error + 1

        if ne.get() and b.get() and a.get() and h.get() and l.get():
            numesp = float(num_esp.get())
            denscamp = float(dens_camp.get())
            ar = float(area.get())
            campomag = float(campo.get())
            comprimento = float(comp.get())
            ind = ((numesp**2)*denscamp*ar)/(campomag*comprimento)
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=530, y=420, width=215, height=50)
            Label(ini, text='Indutância = {:.4e}H'.format(ind), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=535, y=425, width=205, height=40)
        elif error == 0:
            erro()
            error = error + 1
         
        if ne.get() and u.get() and a.get() and l.get():
            numesp = float(num_esp.get())
            mig = float(mi.get())
            ar = float(area.get())
            comprimento = float(comp.get())
            ind = ((numesp**2)*mig*ar)/(comprimento)
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=530, y=420, width=215, height=50)
            Label(ini, text='Indutância = {:.4e}H'.format(ind), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=535, y=425, width=205, height=40)
        elif error == 0:
            erro()     
            error = error + 1

    Button(ini, text = 'Calcular', font = fonte14, command = calcular3, background = '#FFFFFF', foreground = '#343541').place(x = 670, y = 500, width = 100, height = 30)

#Perdas em Converção de Energia
def perdas():
    print('Perdas')

#Cálculo de Energia em Converção de Energia
def energia():
    print('Energia')

#Cálculo de Densidade de campo magnetico
def bh():
    Label(ini, text='', background='#525253', foreground='#FFFFFF', anchor=W).place(x=250, y=326, width=525, height=210)
    Label(ini, text='', background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=250, y=286, width=525, height=40)
    Label(ini, text='Conversão de Energia', font=fonte10, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(
        x=610, y=293, width=140, height=25)
    Label(ini, text='B = uH', font=fonte20, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=300, y=290, width=200, height=35)
    # Botão de voltar
    def voltar3():
        bloco3()

    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image=imagem_vlt, command=voltar3).place(x=745, y=295, width=20, height=20)

    # Enunciado
    Label(ini, text='Clique nas variáveis que você já sabe:', font=fonte15, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=350, y=330, width=350, height=30)

    # INSERINDO AS VARIÁVEIS
    def checkbox_B():
        b == True

    def checkbox_H():
        h==True

    def checkbox_ur():
        ur==True


    b = BooleanVar()
    h = BooleanVar()
    ur = BooleanVar()

    Checkbutton(ini, text="", variable=b, command=checkbox_B, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=355, width=25, height=25)
    Label(ini, text='Densidade de Campo (B)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=355, width=200, height=25)
    dens_camp = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    dens_camp.place(x=485, y=358, width=50, height=20)

    Checkbutton(ini, text="", variable=h, command=checkbox_H, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=385, width=25, height=25)
    Label(ini, text='Campo Magnético (H)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=385, width=185, height=25)
    camp_mag = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    camp_mag.place(x=485, y=388, width=50, height=20)

    Checkbutton(ini, text="", variable=ur, command=checkbox_ur, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=415, width=25, height=25)
    Label(ini, text='Mi relativo (ur)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=415, width=205, height=25)
    mi_r = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    mi_r.place(x=485, y=418, width=50, height=20)

    Label(ini, text='u0 = 4pi x 10^-7', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=445, width=200, height=25)
    

    def calcular5():
        error = 0
        u0 = 4*np.pi*(10**(-7))

        def erro():
            erro_window = Tk()
            erro_window.title('ERRO')
            erro_window.geometry('470x50')  # Aumentei o tamanho da janela de erro
            erro_window.configure(background='#FFFFFF')
            Label(erro_window, text='Não é possível calcular utilizando apenas essas variáveis!', background = '#FFFFFF',foreground = '#000000', anchor = W).place(x=35, y=10, width=500, height=25)
            erro_window.mainloop()

        if h.get() and b.get():      
            dcamp = float(dens_camp.get())
            camph = float(camp_mag.get())
            res = dcamp/(u0*camph)
            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='ur = {}'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
        
        if h.get() and ur.get():      
            camph = float(camp_mag.get())
            mir = float(mi_r.get())
            res = mir*u0*camph
            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='B = {:.4e}T'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
            

        if b.get() and ur.get():      
            dcamp = float(dens_camp.get())
            mir = float(mi_r.get())
            res = dcamp/(u0*mir)
            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='H = {:.4e}Wb/m'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        if error == 0:
            erro()
            


    Button(ini, text='Calcular', font=fonte14, command=calcular5, background='#FFFFFF', foreground='#343541').place(
        x=670, y=500, width=100, height=30)

#Cálculo de Relutância
def relut():
    Label(ini, text='', background='#525253', foreground='#FFFFFF', anchor=W).place(x=250, y=326, width=525, height=210)
    Label(ini, text='', background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=250, y=286, width=525, height=40)
    Label(ini, text='Conversão de Energia', font=fonte10, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(
        x=610, y=293, width=140, height=25)
    Label(ini, text='Relutância', font=fonte20, background='#0a0a41', foreground='#FFFFFF', anchor=W).place(x=300, y=290, width=200, height=35)
    # Botão de voltar
    def voltar3():
        bloco3()

    global imagem_vlt
    diretorio_script = os.path.dirname(__file__)

    caminho_voltar = os.path.join(diretorio_script, "Imagens\imvoltar.png")
    imagemvolt = Image.open(caminho_voltar)
    imagem_vlt = ImageTk.PhotoImage(imagemvolt)
    Button(ini, image=imagem_vlt, command=voltar3).place(x=745, y=295, width=20, height=20)

    # Enunciado
    Label(ini, text='Clique nas variáveis que você já sabe:', font=fonte15, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=350, y=330, width=350, height=30)

    # INSERINDO AS VARIÁVEIS
    def checkbox_R():
        r == True

    def checkbox_l():
        l==True

    def checkbox_A():
        a==True

    def checkbox_ur():
        ur==True


    a = BooleanVar()
    r = BooleanVar()
    ur = BooleanVar()
    l = BooleanVar()

    

    Checkbutton(ini, text="", variable=a, command=checkbox_A, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=355, width=25, height=25)
    Label(ini, text='Área (A)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=355, width=200, height=25)
    area = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    area.place(x=485, y=358, width=50, height=20)

    Checkbutton(ini, text="", variable=r, command=checkbox_R, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=385, width=25, height=25)
    Label(ini, text='Relutância (R)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=385, width=185, height=25)
    relu = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    relu.place(x=485, y=388, width=50, height=20)

    Checkbutton(ini, text="", variable=ur, command=checkbox_ur, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=415, width=25, height=25)
    Label(ini, text='Mi relativo (ur)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=415, width=205, height=25)
    mi_r = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    mi_r.place(x=485, y=418, width=50, height=20)

    Checkbutton(ini, text="", variable=l, command=checkbox_l, background='#525253', foreground='#000000',
                anchor=W).place(x=255, y=445, width=25, height=25)
    Label(ini, text='Comprimento (l)', font=fonte13, background='#525253', foreground='#FFFFFF',
          anchor=W).place(x=275, y=445, width=150, height=25)
    comp = Entry(ini, font=fonte12, background='#FFFFFF', foreground='#343541')
    comp.place(x=485, y=448, width=50, height=20)

    Label(ini, text='u0 = 4pi x 10^-6', font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=275, y=475, width=150, height=25)


    def calcular6():
        error = 0
        u0 = 4*np.pi*(10**(-7))

        def erro():
            erro_window = Tk()
            erro_window.title('ERRO')
            erro_window.geometry('470x50')  # Aumentei o tamanho da janela de erro
            erro_window.configure(background='#FFFFFF')
            Label(erro_window, text='Não é possível calcular utilizando apenas essas variáveis!', background = '#FFFFFF',foreground = '#000000', anchor = W).place(x=35, y=10, width=500, height=25)
            erro_window.mainloop()



        if l.get() and a.get() and r.get():   
            ar = float(area.get())
            re = float(relu.get())
            com = float(comp.get())

            res = com/(u0*ar*re)

            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='ur = {}'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
        if l.get() and a.get() and ur.get():   
            ar = float(area.get())
            mir = float(mi_r.get())
            com = float(comp.get())

            res = com/(mir*u0*ar)

            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='R = {:.4e}H^-1'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
        if a.get() and r.get() and ur.get():   
            ar = float(area.get())
            re = float(relu.get())
            mir = float(mi_r.get())
            
            res = re*u0*mir*ar

            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='l = {:.4e}m'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
        if l.get() and r.get() and ur.get():   
            re = float(relu.get())
            mir = float(mi_r.get())
            com = float(comp.get())
            
            res = com/(mir*u0*re)

            error = error + 1
            Label(ini, text='', font = fonte13, background = '#000000',foreground = '#FFFFFF', anchor = W).place(x=545, y=395, width=215, height=50)
            Label(ini, text='A = {:4e}m^2'.format(res), font = fonte13, background = '#525253',foreground = '#FFFFFF', anchor = W).place(x=550, y=400, width=205, height=40)
        
        
        if error == 0:
            erro()
            


    Button(ini, text='Calcular', font=fonte14, command=calcular6, background='#FFFFFF', foreground='#343541').place(
        x=670, y=500, width=100, height=30)

#Formulário 
def formulas():

    caminho_completo = os.path.abspath(__file__)
    diretorio_atual = os.path.dirname(caminho_completo)
    nome_arquivo = "arquivos\conversao_formulario.txt"
    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            os.system(f"notepad.exe {caminho_arquivo}") 
    except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except UnicodeDecodeError as e:
            print(f"Erro de decodificação Unicode: {e}")


#-------------------------------------

#============== Interfaçe Inicial =============#

ini = Tk()
ini.title('Central de Engenharia Elétrica')
ini.geometry('1000x550')
ini.configure(background='#9f9fa7')

#----------------------------------------------------------------------------------------

#FONTES >
f20 = int(20) #Tamanho da Fonte do título
fonte20 = font.Font(family="Arial", size=f20) #Fonte

f19 = int(19) #Tamanho da Fonte do título
fonte19 = font.Font(family="Arial", size=f19) #Fonte

f18 = int(18) #Tamanho da Fonte do título
fonte18 = font.Font(family="Arial", size=f18) #Fonte

f17 = int(17) #Tamanho da Fonte do título
fonte17 = font.Font(family="Arial", size=f17) #Fonte

f16 = int(16) #Tamanho da Fonte do texto
fonte16 = font.Font(family="Arial", size=f16) #Fonte

f15 = int(15) #Tamanho da Fonte do texto
fonte15 = font.Font(family="Arial", size=f15) #Fonte

f14 = int(14) #Tamanho da Fonte do texto
fonte14 = font.Font(family="Arial", size=f14) #Fonte

f13 = int(13) #Tamanho da Fonte do texto
fonte13 = font.Font(family="Arial", size=13) #Fonte

f12 = int(12) #Tamanho da Fonte do texto
fonte12 = font.Font(family="Arial", size=12) #Fonte

f11 = int(11) #Tamanho da Fonte do texto
fonte11 = font.Font(family="Arial", size=11) #Fonte

f10 = int(10) #Tamanho da Fonte do texto
fonte10 = font.Font(family="Arial", size=f10) #Fonte
#< FONTES 

#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------

bloco1()
bloco2()
bloco3()
bloco4()

#----------------------------------------------------------------------------------------
ini.mainloop()



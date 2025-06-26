from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import os
import tkinter

# Cores
co0 = "#000000"
co1 = "#feffff"
co2 = "#38576b"
co3 = "#38576b"
co4 = "#403d3d"

# Janela principal
janela = Tk()
janela.title("Login com Cadastro")
janela.geometry("310x350")
janela.configure(bg=co1)
janela.resizable(False, False)

# Lista de credenciais
credenciais = ['Pedro', '123']

# Frames
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Título
l_nome = Label(frame_cima, text="🔐 LOGIN", height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(relx=0.5, rely=0.3, anchor=CENTER)
l_linha = Label(frame_cima, width=300, text="", height=1, bg=co2)
l_linha.place(relx=0.5, rely=0.9, anchor=CENTER)

# Funções
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!!!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', f'Seja bem-vindo de volta {credenciais[0]}')
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
        mostrar_mensagem_boas_vindas(credenciais[0])
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuário ou a senha.')

def mostrar_mensagem_boas_vindas(nome):
    nova_janela()
    mensagem = f"Seja bem-vindo de volta, {nome}!"
    mensagem_label = Label(frame_cima, text="", font=('Arial', 14, 'bold'), bg=co1, fg=co4)
    mensagem_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def escrever(i=0):
        if i < len(mensagem):
            mensagem_label.config(text=mensagem[:i+1])
            frame_cima.after(80, escrever, i+1)

    escrever()

def cadastrar_usuario():
    nome = e_nome.get()
    senha = e_pass.get()
    if nome == '' or senha == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos para cadastrar.')
    elif nome == credenciais[0]:
        messagebox.showwarning('Erro', 'Esse usuário já existe.')
    else:
        credenciais[0] = nome
        credenciais[1] = senha
        messagebox.showinfo('Cadastro', f'Usuário "{nome}" cadastrado com sucesso!')

def nova_janela():
     estilo_botao = {'width': 25, 'height': 2, 'bg': co3, 'fg': co1,'font': ('Ivy 10 bold'), 'relief': RAISED, 'overrelief': RIDGE}

     menu_entrada = Label(frame_baixo, text="Menu de Aplicativos", font=('Arial', 14, 'bold'), bg=co1, fg=co4).place(relx=0.5, y=0, anchor=N)

     botao_calc = Button(frame_baixo, text="🧮Abrir Calculadora", width=25, height=2, bg=co3, fg=co1,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_calculadora)
     botao_calc.place(relx=0.5, y=40, anchor=N)
     botao_calc = Button(frame_baixo, text="💪Abrir Calculadora de IMC", width=25, height=2, bg=co3, fg=co1,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_calculadoraIMC)
     botao_calc.place(relx=0.5, y=90, anchor=N)
     botao_calc = Button(frame_baixo, text="🎨Abrir Aplicativo de cores", width=25, height=2, bg=co3, fg=co1,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_cores)
     botao_calc.place(relx=0.5, y=140, anchor=N)

     Label(frame_baixo, text="Clique em um botão para abrir o app", bg=co1, fg=co4, font=('Arial', 10)).place(relx=0.5, y=200, anchor=N)


def abrir_calculadora():
# Aqui vai o conteúdo completo da científica
        co1 = '#feffff'
        co2 = '#6f9fbd'
        co3 = '#38576b'

        fundo = '#e8e6e6'
        co10 = '#363434'
        cor11 = '#424345'

        cor1 = '#ffab40'
        cor2 = '#ff333a'
        cor3 = '#6bd66f'
        cor4 = '#ab8918'

        #janela
        janela = Tk()
        janela.title('')
        janela.geometry('235x289')
        janela.configure(bg=co1)


        style = ttk.Style(janela)
        style.theme_use("clam")

        # FRAMES

        ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

        frame_score = Frame(janela, width=300, height=56, bg=co3, pady=0, padx=0, relief="flat")
        frame_score.grid(row=1, column=0, stick=NW)

        frame_cientifica = Frame(janela, width=300, height=86, bg=co3, pady=0, padx=0, relief="flat")
        frame_cientifica.grid(row=2, column=0, stick=NW)

        frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat",)
        frame_quadros.grid(row=3, column=0, stick=NW)

        # funções

        def entering_values(event):
            global all_values
            all_values = all_values + str(event)
            value_text.set(all_values)

        def calculate():
            global all_values
            global texto
            texto = all_values

            modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.log10', 'math.e', 'math.pow', 'math.pi', 'math.radian']

            for i in modulos:
                if i == 'math.tan':
                    texto = texto.replace("tan", i)
                if i == 'math.sin':
                    texto = texto.replace("sin", i)
                if i == 'math.cos':
                    texto = texto.replace("cos", i)
                if i == 'math.sqrt':
                    texto = texto.replace("sqrt", i)

                #------------------------------------

                if i == 'math.log':
                    texto = texto.replace("log", i)
                if i == 'math.log10':
                    texto = texto.replace("log10", i)
                if i == 'math.e':
                    texto = texto.replace("e", i)
                if i == 'math.pow':
                    texto = texto.replace("pow", i)

                #------------------------------------

                if i == 'math.radians':
                    texto = texto.replace("rad", i)
                if i == 'math.pi':
                    texto = texto.replace("pi", i)

            result = str(eval(texto))

            print(result)
            print(texto)

            value_text.set(result)
            all_values = ""

        def scream_clear():
            global all_values
            all_values = ""
            value_text.set("")

        all_values = ""

        value_text = StringVar()

        app_scream = Label(frame_score, width=16, height=2, textvariable= value_text, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474f', fg=co1)
        app_scream.place(x=0, y=0)

        # buttons
        b_tan = Button(frame_cientifica, text="tan", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('tan'))
        b_tan.place(x=0, y=1)

        b_sin = Button(frame_cientifica, text="sin", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('sin'))
        b_sin.place(x=59, y=1)

        b_cos = Button(frame_cientifica, text="cos", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('cos'))
        b_cos.place(x=118, y=1)

        b_sqrt = Button(frame_cientifica, text="sqrt", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('sqrt'))
        b_sqrt.place(x=177, y=1)

        b_log = Button(frame_cientifica, text="log", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('log'))
        b_log.place(x=0, y=30)

        b_log10 = Button(frame_cientifica, text="log10", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('log10'))
        b_log10.place(x=59, y=30)

        b_euler = Button(frame_cientifica, text="e", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('e'))
        b_euler.place(x=118, y=30)

        b_pow = Button(frame_cientifica, text="pow", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('pow'))
        b_pow.place(x=177, y=30)

        b_12 = Button(frame_cientifica, text="pi", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('pi'))
        b_12.place(x=0, y=58)

        b_13 = Button(frame_cientifica, text=",", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(','))
        b_13.place(x=59, y=58)

        b_14 = Button(frame_cientifica, text="(", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('('))
        b_14.place(x=118, y=58)

        b_15 = Button(frame_cientifica, text=")", width=6, height=1, bg=co10, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(')'))
        b_15.place(x=177, y=58)

        b_1 = Button(frame_quadros, text="C", width=14, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:scream_clear())
        b_1.place(x=0, y=0)

        b_2 = Button(frame_quadros, text="%", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('%'))
        b_2.place(x=118, y=0)

        b_3 = Button(frame_quadros, text="/", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('/'))
        b_3.place(x=177, y=0)

        b_4 = Button(frame_quadros, text="7", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(7))
        b_4.place(x=0, y=29)

        b_5 = Button(frame_quadros, text="8", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(8))
        b_5.place(x=59, y=29)

        b_6 = Button(frame_quadros, text="9", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(9))
        b_6.place(x=118, y=29)

        b_7 = Button(frame_quadros, text="*", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('*'))
        b_7.place(x=177, y=29)

        b_8 = Button(frame_quadros, text="4", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(4))
        b_8.place(x=0, y=58)

        b_9 = Button(frame_quadros, text="5", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(5))
        b_9.place(x=59, y=58)

        b_10 = Button(frame_quadros, text="6", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(6))
        b_10.place(x=118, y=58)

        b_11 = Button(frame_quadros, text="-", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('-'))
        b_11.place(x=177, y=58)

        b_12 = Button(frame_quadros, text="1", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(1))
        b_12.place(x=0, y=87)

        b_13 = Button(frame_quadros, text="2", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(2))
        b_13.place(x=59, y=87)

        b_14 = Button(frame_quadros, text="3", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(3))
        b_14.place(x=118, y=87)

        b_15 = Button(frame_quadros, text="+", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('+'))
        b_15.place(x=177, y=87)

        b_16 = Button(frame_quadros, text="0", width=14, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values(0))
        b_16.place(x=0, y=116)

        b_17 = Button(frame_quadros, text=".", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_values('.'))
        b_17.place(x=118, y=116)

        b_18 = Button(frame_quadros, text="=", width=6, height=1, bg=cor11, fg=fundo, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:calculate())
        b_18.place(x=177, y=116)

def abrir_calculadoraIMC():
    from tkinter import Tk, ttk, messagebox
    

    #cores
    co0 =  '#ffffff'
    co1 =  '#1c1c1c'
    co2 = '#4065a1'
    co3 = '#4f4f4f'

    janela = Tk()
    janela.title('')
    janela.geometry('295x230')
    janela.configure(bg=co0)

    frame_cima = Frame(janela, width=295, height=60, bg=co0, pady=1, padx=0, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=400, height=230, bg=co0, pady=1, padx=0, relief="flat")
    frame_baixo.grid(row=1, column=0, sticky=NSEW)

    # configurando frame_cima
    app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16'), bg=co0, fg=co1)
    app_nome.place(x=0, y=0)

    app_nome = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
    app_nome.place(x=0, y=35)

    def calcular():
        peso = float(e_peso.get())
        altura = float(e_altura.get())

        imc = peso / altura**2

        resultado = imc

        if resultado < 18.5:
            l_resultado_texto['text'] = "Abaixo do peso"
        elif resultado >= 18.5 and resultado < 25:
            l_resultado_texto['text'] = "Peso normal"
        elif resultado >= 25 and resultado < 29.9:
            l_resultado_texto['text'] = "Sobrepeso"
        elif resultado >= 30 and resultado < 34.9:
            l_resultado_texto['text'] = "Obesidade grau 1"
        elif resultado >= 35 and resultado < 39.9:
            l_resultado_texto['text'] = "Obesidade grau 2"
        else:
            l_resultado_texto['text'] = "Obesidade (Mórbida)"

        l_resultado['text'] = "{:.{}f}".format(resultado, 2)


    l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
    l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

    e_peso = Entry(frame_baixo,width=5 ,relief='solid', font=('Ivy 10 bold '), justify='center')
    e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


    l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
    l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

    e_altura = Entry(frame_baixo,width=5 ,relief='solid', font=('Ivy 10 bold '), justify='center')
    e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

    l_resultado = Label(frame_baixo, text='---', width=5 ,height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0)
    l_resultado.place(x=170, y=10)

    l_resultado_texto = Label(frame_baixo, text='', width=37 ,height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
    l_resultado_texto.place(x=0, y=90)

    b_calcular = Button(frame_baixo,command=calcular, text='Calcular', width=34 ,height=1,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0)
    b_calcular.grid(row=4, column=0, sticky=NSEW, pady=50, padx=5, columnspan=30)

def abrir_cores():
    from tkinter import Tk, ttk, messagebox
    import tkinter.messagebox

    cor0 = "#444466"  # Pret0 / black
    cor1 = "#feffff"  # branco / white
    cor2 = "#004338"


    janela = Tk()
    janela.geometry("600x205")
    janela.configure(bg=cor1)


    tela = Label(janela, bg = cor0, width = 40, height= 10, bd=1)
    tela.grid(row= 0, column=0)


    frame_direita = Frame(janela, bg=cor1)
    frame_direita.grid(row= 0, column=1, padx=5)


    frame_baixo = Frame(janela, bg=cor1)
    frame_baixo.grid(row= 1, column=0, columnspan=2, pady=15)


    def escala(valor):
        r=s_red.get()
        g=s_green.get()
        b=s_blue.get()
                                                                                                                                                                                            

        rgb = f'{r}, {g}, {b}'


        hexadecimal = "#%02x%02x%02x" % (r, g, b)


        tela['bg'] = hexadecimal


        e_cor.delete(0,END)
        e_cor.insert(0,hexadecimal)



    def onCLick():
        tkinter.messagebox.showinfo('Cor', "a cor foi copiada")


        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(e_cor.get())
        clip.destroy()


    l_red = Label(frame_direita, text='Red', width=7, bg=cor1, fg='red', anchor='nw', font = ("Time New Roman", 12, "bold"))
    l_red.grid(row= 0, column=0)
    s_red=Scale(frame_direita, command= escala, from_=0, to=255, bg=cor1,fg="red", orient=HORIZONTAL)
    s_red.grid(row= 0, column=1)


    l_green = Label(frame_direita, text='Green', width=7, bg=cor1, fg='green', anchor='nw', font = ("Time New Roman", 12, "bold"))
    l_green.grid(row= 1, column=0)
    s_green=Scale(frame_direita, command= escala, from_=0, to=255, bg=cor1,fg="green", orient=HORIZONTAL)
    s_green.grid(row= 1, column=1)


    l_blue = Label(frame_direita, text='Blue', width=7, bg=cor1, fg='blue', anchor='nw', font = ("Time New Roman", 12, "bold"))
    l_blue.grid(row= 2, column=0)
    s_blue=Scale(frame_direita, command= escala, from_=0, to=255, bg=cor1,fg="blue", orient=HORIZONTAL)
    s_blue.grid(row= 2, column=1)


    l_rgb = Label(frame_baixo, text="CÓDIGO HEX : ", bg=cor1, font=("Ivy", 10,"bold"))
    l_rgb.grid(row= 0, column=0, padx= 5)


    e_cor = Entry(frame_baixo, bg=cor1, font=("Ivy", 10,"bold"), justify=CENTER)
    e_cor.grid(row= 0, column=1, padx= 5)


    b_copiar = Button(frame_baixo, text="Copiar a cor", bg=cor1, font=("Ivy", 8,"bold"), relief=RAISED, overrelief= RIDGE)
    b_copiar.grid(row= 0, column=2, padx= 5)


    l_app_nome = Label(frame_baixo, text="Seletor de cores", bg=cor1, font=("Ivy", 15,"bold"))
    l_app_nome.grid(row= 0, column=3, padx= 40)


# Campos de entrada
l_nome = Label(frame_baixo, text="Nome 👤", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="Senha 🔒", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=15, y=130)

# Botões
botao_confirmar = Button(frame_baixo, text="Entrar ➡", width=39, height=2, bg=co2, fg=co1,font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=180)

botao_cadastrar = Button(frame_baixo, text="Cadastrar ✔", width=39, height=2, bg=co3, fg=co1,font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=cadastrar_usuario)
botao_cadastrar.place(x=15, y=230)

janela.mainloop()
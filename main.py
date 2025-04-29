import tkinter as tk
tela_texto = "   "

def add_tela_texto (sth):
    global tela_texto
    tela_texto= tela_texto + str(sth)
    tela.delete("1.0", "end")
    tela.insert("1.0", tela_texto)
def calculadora():
    global tela_texto
    resultado = str(eval(tela_texto))
    tela.delete("1.0", "end")
    tela.insert("1.0", resultado)
def zerar():
    global tela_texto 
    tela_texto=""
    tela.delete("1.0", "end")

janela=tk.Tk()
janela.geometry("300x310")
tela = tk.Text(janela, height=2,width=21,font=("Comic Sans", 20))
tela.grid(row=1, column=1,columnspan=4)
# Os botões da frente
btn_1=tk.Button(janela,text="1",command=lambda: add_tela_texto(1),width=5,font=("Comic Sans",14))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(janela,text="2",command=lambda: add_tela_texto(2),width=5,font=("Comic Sans",14))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(janela,text="3",command=lambda: add_tela_texto(3),width=5,font=("Comic Sans",14))
btn_3.grid(row=4,column=3)

btn_4=tk.Button(janela,text="4",command=lambda: add_tela_texto(4),width=5,font=("Comic Sans",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(janela,text="5",command=lambda: add_tela_texto(5),width=5,font=("Comic Sans",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(janela,text="6",command=lambda: add_tela_texto(6),width=5,font=("Comic Sans",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(janela,text="7",command=lambda: add_tela_texto(7),width=5,font=("Comic Sans",14))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(janela,text="8",command=lambda: add_tela_texto(8),width=5,font=("Comic Sans",14))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(janela,text="9",command=lambda: add_tela_texto(9),width=5,font=("Comic Sans",14))
btn_9.grid(row=2,column=3)

btn_0=tk.Button(janela,text="0",command=lambda: add_tela_texto(0),width=5,font=("Comic Sans",14))
btn_0.grid(row=5,column=1)
# Os operadores
btn_plus=tk.Button(janela,text="+",command=lambda: add_tela_texto("+"),width=5,font=("Comic Sans",14))
btn_plus.grid(row=4,column=4)

btn_minus=tk.Button(janela,text="-",command=lambda: add_tela_texto("-"),width=5,font=("Comic Sans",14))
btn_minus.grid(row=5,column=4)

btn_times=tk.Button(janela,text="*",command=lambda: add_tela_texto("*"),width=5,font=("Comic Sans",14))
btn_times.grid(row=3,column=4)

btn_division=tk.Button(janela,text="/",command=lambda: add_tela_texto("/"),width=5,font=("Comic Sans",14))
btn_division.grid(row=2,column=4)

btn_clear=tk.Button(janela,text="clear",command=lambda: zerar(),width=5,font=("Comic Sans",14))
btn_clear.grid(row=5,column=3)

btn_decimal=tk.Button(janela,text=".",command=lambda: add_tela_texto("."),width=5,font=("Comic Sans",14))
btn_decimal.grid(row=5,column=2)

btn_open_parenthesis=tk.Button(janela,text="(",command=lambda: add_tela_texto("("),width=5,font=("Comic Sans",14))
btn_open_parenthesis.grid(row=6,column=1)

btn_close_parenthesis=tk.Button(janela,text=")",command=lambda: add_tela_texto(")"),width=5,font=("Comic Sans",14))
btn_close_parenthesis.grid(row=6,column=2)

btn_equal=tk.Button(janela,text="=",command=lambda: calculadora(),width=13,font=("Comic Sans",14))
btn_equal.grid(row=6,column=3,columnspan=2)

janela.mainloop()

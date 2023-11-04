from tkinter import Button, Tk, Frame, Entry,END

# hover

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        self["background"] = self["activebackground"]
    
    def on_leave(self, e):
        self["background"] = self.defaultBackground

class calculadora():
    Resultado = None
    def __init__(self):
        ventana = Tk()
        ventana.geometry('274x328')
        ventana.config(bg="white")
        # ventana.iconbitmap(bitmap='icono.ico')
        ventana.resizable(0,0)
        ventana.title("Calculadora")
        
        frame = Frame(ventana, bg="black", relief="raised")
        frame.grid(column=0, row=0, padx=6, pady=3)

        self.Resultado = Entry(frame, bg="#9EF8E8", width=18, relief="groove", font="Montserrat 16", justif="right")
        self.Resultado.grid(columnspan=4, row=0, padx=1, pady=3, ipadx=1, ipady=1)

        # fila 1
        # van 1, 2, 3, eliminar
        Button1 = HoverButton(frame, text="1", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(1))
        Button1.grid(column=0, row=1, padx=3, pady=3)

        Button1 = HoverButton(frame, text="2", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(2))
        Button1.grid(column=1, row=1, padx=3, pady=3)

        Button1 = HoverButton(frame, text="3", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(3))
        Button1.grid(column=2, row=1, padx=3, pady=3)

        Button1 = HoverButton(frame, text="⌫", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.borrar_uno())
        Button1.grid(column=3, row=1, padx=3, pady=3)

        # fila 2
        # van 4, 5, 6, +
        Button1 = HoverButton(frame, text="4", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(4))
        Button1.grid(column=0, row=2, padx=3, pady=3)

        Button1 = HoverButton(frame, text="5", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(5))
        Button1.grid(column=1, row=2, padx=3, pady=3)

        Button1 = HoverButton(frame, text="6", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(6))
        Button1.grid(column=2, row=2, padx=3, pady=3)

        Button1 = HoverButton(frame, text="+", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener("+"))
        Button1.grid(column=3, row=2, padx=3, pady=3)

        # fila 3
        # van 7, 8, 9, -

        Button1 = HoverButton(frame, text="7", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(7))
        Button1.grid(column=0, row=3, padx=3, pady=3)

        Button1 = HoverButton(frame, text="8", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(8))
        Button1.grid(column=1, row=3, padx=3, pady=3)

        Button1 = HoverButton(frame, text="9", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(9))
        Button1.grid(column=2, row=3, padx=3, pady=3)

        Button1 = HoverButton(frame, text="-", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener("-"))
        Button1.grid(column=3, row=3, padx=3, pady=3)

        # fila 4 y 5
        # van 0, ., /, *, 
        # van 0, =, =, C

        Button1 = HoverButton(frame, text="0", borderwidth=2, height=5, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener(0))
        Button1.grid(column=0, row=4, rowspan=2, padx=3, pady=3)

        Button1 = HoverButton(frame, text=".", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener("."))
        Button1.grid(column=1, row=4, padx=3, pady=3)

        Button1 = HoverButton(frame, text="/", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener("/"))
        Button1.grid(column=2, row=4, padx=3, pady=3)

        Button1 = HoverButton(frame, text="*", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.obtener("*"))
        Button1.grid(column=3, row=4, padx=3, pady=3)

        Button1 = HoverButton(frame, text="=", borderwidth=2, height=2, width=12, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.operacion())
        Button1.grid(column=1, columnspan=2, row=5, padx=3, pady=3)

        Button1 = HoverButton(frame, text="C", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#999AB8", anchor="center", command=lambda: self.borrar_todo())
        Button1.grid(column=3, columnspan=2, row=5, padx=3, pady=3)

        ventana.mainloop()
    
    i = 0
    def obtener(self, dato):
        self.i += 1
        self.Resultado.insert(self.i, dato)

    def operacion(self):
        ecuacion = self.Resultado.get()
        if self.i != 0:
            try:
                result = str(eval(ecuacion))
                self.Resultado.delete(0, END)
                self.Resultado.insert(0, result)
                longitud = len(result)
                self.i = longitud
                
            except:
                result = "ERROR"
                self.Resultado.delete(0, END)
                self.Resultado.insert(0, result)
        else:
            pass

    def borrar_uno(self):
        if self.i > 0 : self.i -= 1
        self.Resultado.delete(self.i, END)

    def borrar_todo(self):
        self.Resultado.delete(0, END)
        self.i = 0    

calculadora = calculadora()
import customtkinter as ctk
import ctypes
import os
from PIL import Image
import MSED

def fix_taskbar_icon():
    my_appid = 'u_pamplona.matematicas.mi_app.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)

def validar_numeros(texto_nuevo):
    if texto_nuevo == "":
        return True
    if texto_nuevo == "-":
        return True
    try:
        int(texto_nuevo)
        return True
    except ValueError:
        return False

class Menu(ctk.CTkFrame):
    def __init__(self, master, titulo, opciones, comando_seleccion, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.abierto = False
        self.comando_seleccion = comando_seleccion

         # Carga de iconos 
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        img_der_pil = Image.open(os.path.join(ruta_base,"..", "assets", "flecha_derecha.png"))
        self.img_derecha = ctk.CTkImage(light_image=img_der_pil, size=(12, 12))
        
        img_aba_pil = Image.open(os.path.join(ruta_base,"..", "assets", "flecha_abajo.png"))
        self.img_abajo = ctk.CTkImage(light_image=img_aba_pil, size=(12, 12))

        # Boton titulo
        self.btn_texto = ctk.CTkButton(
            self, 
            text=titulo, 
            anchor="w",
            font=("Segoe UI", 13, "bold"),
            fg_color="transparent",
            hover_color="gray30",
            command=self.toggle_menu 
        )
        self.btn_texto.grid(row=0, column=0, sticky="ew")

        # Botón Flecha 
        self.btn_flecha = ctk.CTkButton(
            self,
            text="",
            image=self.img_derecha,
            width=30, 
            fg_color="gray40",
            hover_color="gray30",
            command=self.toggle_menu 
        )
        self.btn_flecha.grid(row=0, column=1, padx=2)

        # Configurar las columnas de este Frame
        self.grid_columnconfigure(0, weight=1)

        # Opciones
        self.frame_opciones = ctk.CTkFrame(self, fg_color="transparent")
        for opcion in opciones:
            ctk.CTkButton(
                self.frame_opciones,
                text=opcion,
                anchor="w",
                fg_color="transparent",
                font=("Segoe UI", 13, "bold"), 
                hover_color="gray30",
                # Usamos lambda para pasar el nombre de la opción al comando
                command=lambda opt=opcion: self.comando_seleccion(opt)).pack(fill="x", padx=10, pady=1)

    def toggle_menu(self):
        if self.abierto:
            self.frame_opciones.grid_forget()
            self.btn_flecha.configure(image=self.img_derecha)
        else:
            self.frame_opciones.grid(row=1, column=0, columnspan=2, sticky="nsew")
            self.btn_flecha.configure(image=self.img_abajo)
        self.abierto = not self.abierto

class Frame1(ctk.CTkScrollableFrame):
    def __init__(self, master, comando_cambio, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # Menu 1
        self.menu1 = Menu(
            self, 
            "Divisibilidad en \u2124", 
            ["Algoritmo de la División", "Algoritmo de Euclides", "Maxímo Común Divisor", "Lema de Bezout"],
            comando_seleccion=comando_cambio)
        self.menu1.pack(fill="x", padx=(10, 5), pady=5)

        # Menu 2
        self.menu2 = Menu(
            self, 
            "Divisibilidad en \u2124\u2099", 
            ["Algoritmo de la División en \u2124\u2099", "Algoritmo de Euclides en \u2124\u2099", "Maxímo Común Divisor en \u2124\u2099", "Lema de Bezout en \u2124\u2099"],
            comando_seleccion=comando_cambio)
        self.menu2.pack(fill="x", padx=(10, 5), pady=5)

        # Menu 3
        self.menu3 = Menu(
            self, 
            "Ecuaciones Diofánticas Lineales en \u2124\u2099",
            ["Metodo de la Falsa Posición", "Metodo del Algoritmo de Euclides y Lema de Bezout", "Metodo de Diofanto"],
            comando_seleccion=comando_cambio)
        self.menu3.pack(fill="x", padx=(10, 5), pady=5)

        # Menu 4
        self.menu4 = Menu(
            self, 
            "Ternas en \u2124\u2099", 
            ["Ternas con el Metodo de Diofanto", "Metodo de Fibonacci"],
            comando_seleccion=comando_cambio)
        self.menu4.pack(fill="x", padx=(10, 5), pady=5)

class Frame_Algoritmo_Division(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="ALGORITMO DE LA DIVISIÓN EN \u2124",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="a",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="b",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="17",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="6",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            if b == 0:
                self.resultado.configure(text="Error: b no puede ser 0", text_color="red")
                return
            q,r =MSED.algoritmo_division(a, b)
            respuesta = f" {a} = ({b} × {q}) + {r} "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")

class Frame_Algoritmo_Euclides(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="ALGORITMO DE EUCLIDES EN \u2124",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="a",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="b",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="28",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="12",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())

            if (b == 0):
                self.resultado.configure(text="Error: b no puede ser 0", text_color="red")
                return
            
            d, cocientes, residuos = MSED.algoritmo_euclides(a, b)
            respuesta = ""
            temp_a = a
            temp_b =b
            for q, r in zip(cocientes, residuos):
                respuesta += f"{temp_a} = ({temp_b} × {q}) + {r}\n"
                temp_a = temp_b
                temp_b = r 

            if (r!=0):
                q1,r1 = MSED.algoritmo_division(temp_a,r)
                respuesta += f"{temp_a} = ({r} × {q1}) + {r1}\n"

            respuesta += f"\nEl MCD es: {d}"  
            self.resultado.configure(text=respuesta, text_color="#5fb3b3", justify="left")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")

class Frame_Maximo_Comun_Divisor(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="MAXIMO COMUN DIVISOR EN \u2124 ",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="a",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="b",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="17",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="6",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            d =MSED.mcd(a, b)
            respuesta = f"mcd({a},{b}) = {d}"
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")

class Frame_Lema_Bezout(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="LEMA DE BEZOUT EN \u2124",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="a",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="b",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="17",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="6",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            d, x, y =MSED.lema_bezout(a, b)
            respuesta = f" {a}({x}) + {b}({y}) = {d} "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")  

class Frame_Algoritmo_Division_zn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="ALGORITMO DE LA DIVISIÓN EN \u2124\u2099",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (modulo)
        self.texto4 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="3",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="2",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="5",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=3, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            q,r =MSED.algoritmo_division_zn(a, b, n)
            respuesta = f" [{a}] = ([{b}] × [{q}]) + [{r}] "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clases de equivalencia modulo n", text_color="red")

class Frame_Algoritmo_Euclides_zn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="ALGORITMO DE EUCLIDES EN \u2124\u2099",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto4 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="18",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="5",
            validate="key",        
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,5), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=3, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            d, cocientes, residuos = MSED.algoritmo_euclides_zn(a, b, n)
            respuesta = ""
            temp_a = a
            temp_b =b
            for q, r in zip(cocientes, residuos):
                respuesta += f"[{temp_a}] = [{temp_b}] × [{q}] + [{r}]\n"
                temp_a = temp_b
                temp_b = r 
            if (r!=0):
                q1,r1 = MSED.algoritmo_division_zn(temp_a,r,n)
                respuesta += f"[{temp_a}] = [{r}] × [{q1}] + [{r1}]\n"
            respuesta += f"\nEl MCD es: [{d}]"  
            self.resultado.configure(text=respuesta, text_color="#5fb3b3", justify="left")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")

class Frame_Maximo_Comun_Divisor_zn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="MAXIMO COMUN DIVISOR EN \u2124\u2099 ",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto4 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="12",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="6",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="15",
            validate="key",        # Validar en cada pulsación de tecla
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=3, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            d =MSED.MCD(a, b, n)
            respuesta = f"MCD([{a}],[{b}]) = [{d}]"
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red")

class Frame_Lema_Bezout_zn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="LEMA DE BEZOUT EN \u2124\u2099",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto4 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=3, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            d, x, y =MSED.lema_bezout_zn(a, b, n)
            respuesta = f" [{a}]× [{x}] + [{b}]× [{y}] = [{d}] "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese números enteros", text_color="red") 

class Frame_Falsa_Posicion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO DE LA FALSA POSICIÓN",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (c)
        self.texto4 = ctk.CTkLabel(
            self,
            text="[c]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto5 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto5.grid(row=1, column=3, padx=0, pady=1, sticky="ew")

        # TEXTO (x1)
        self.texto6 = ctk.CTkLabel(
            self,
            text="[x1]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto6.grid(row=3, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (y1)
        self.texto7 = ctk.CTkLabel(
            self,
            text="[y1]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto7.grid(row=3, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (c)
        self.entry_c = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_c.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=3, padx=(5,10), pady=10, sticky="ew")

        # Entrada (x1)
        self.entry_x1 = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_x1.grid(row=3, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (y1)
        self.entry_y1 = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_y1.grid(row=3, column=3, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=5, column=0, columnspan=4, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            c = int(self.entry_c.get())
            n = int(self.entry_n.get())
            x1= int(self.entry_x1.get())
            y1= int(self.entry_y1.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            s = MSED.hay_solucion(a,b,c,n)
            if (s == False):
                self.resultado.configure(text="No hay solucion para la ecuacion diofantica lineal en Zn", text_color="red")
                return
            d= a*x1 + b*y1
            q0,d= MSED.algoritmo_division(d,n)
            if (d==0):
                self.resultado.configure(text="[x1],[y1] deben cumplir que si [a][x1]+[b][y1]=[d], entonces:\n [d] debe ser unidad en Zn, o  \n  mcd(d,n) debe dividir a c", text_color="red")
                return
            m = MSED.mcd(d,n)
            q,r= MSED.algoritmo_division(c,d)
            if (m!=1 and r!=0):
                self.resultado.configure(text="[x1],[y1] deben cumplir que si [a][x1]+[b][y1]=[d], entonces:\n [d] debe ser unidad en Zn, o  \n  mcd(d,n) debe dividir a c", text_color="red")
                return
            x, y =MSED.falsa_posicion(a, b, c, n, x1, y1)
            respuesta = f" [{a}]× [{x}] + [{b}]× [{y}] = [{c}] "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clases de equivalencia modulo n", text_color="red")

class Frame_Euclides_Bezout(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO DEL ALGORITMO DE EUCLIDES Y LEMA DE BEZOUT",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (c)
        self.texto4 = ctk.CTkLabel(
            self,
            text="[c]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto5 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto5.grid(row=1, column=3, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (c)
        self.entry_c = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_c.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=3, padx=(5,10), pady=10, sticky="ew")


        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=4, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            c = int(self.entry_c.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            s = MSED.hay_solucion(a,b,c,n)
            if (s == False):
                self.resultado.configure(text="No hay solucion para la ecuacion diofantica lineal en Zn", text_color="red")
                return
            x, y =MSED.euclides_bezout(a, b, c, n)
            respuesta = f" [{a}]× [{x}] + [{b}]× [{y}] = [{c}] "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clases de equivalencia modulo n", text_color="red")

class Frame_Diofanto(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO DE DIOFANTO",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

        # TEXTO (a)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[a]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (b)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[b]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (c)
        self.texto4 = ctk.CTkLabel(
            self,
            text="[c]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto4.grid(row=1, column=2, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto5 = ctk.CTkLabel(
            self,
            text="n",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto5.grid(row=1, column=3, padx=0, pady=1, sticky="ew")

        # TEXTO (t)
        self.texto6 = ctk.CTkLabel(
            self,
            text="[t]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto6.grid(row=1, column=4, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (a)
        self.entry_a = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_a.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (b)
        self.entry_b = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_b.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Entrada (c)
        self.entry_c = ctk.CTkEntry(
            self,
            placeholder_text="55",
            validate="key",        
            validatecommand=vcmd)
        self.entry_c.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=3, padx=(5,10), pady=10, sticky="ew")

        # Entrada (t)
        self.entry_t = ctk.CTkEntry(
            self,
            placeholder_text="1",
            validate="key",        
            validatecommand=vcmd)
        self.entry_t.grid(row=2, column=4, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=5, pady=5)

    def calcular(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            c = int(self.entry_c.get())
            n = int(self.entry_n.get())
            t = int (self.entry_t.get())
            m1= MSED.MCD(a,b,n)
            a= a//m1
            b= b//m1
            c= c//m1
            n= n//m1
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            s = MSED.hay_solucion(a,b,c,n)
            if (s == False):
                self.resultado.configure(text="No hay solucion para la ecuacion diofantica lineal en Zn", text_color="red")
                return
            m, cocientes, residuos = MSED.algoritmo_euclides_zn(b,a,n)
            if (residuos[-1] != 1):
                self.resultado.configure(text="El Metodo de Diofanto no es aplicable", text_color="red")
                return
            x, y = MSED.diofanto(a, b, c, n, t)
            print(a)
            respuesta = f" [{a*m1}]× [{x}] + [{c*m1}] = [{b*m1}]× [{y}] "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clases de equivalencia modulo n", text_color="red")

class Frame_ternas_Diofanto_1(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO DE DIOFANTO PARA ENCONTRAR TERNAS CON [M]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (m)
        self.texto1 = ctk.CTkLabel(
            self,
            text="[m]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto1.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[n]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (m)
        self.entry_m = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_m.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            m = int(self.entry_m.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            x, y, z = MSED.ternas_Diofanto1(m, n)
            respuesta = f" [{x}]\u00B2 + [{y}]\u00B2 = [{z}]\u00B2 "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clase de equivalencia modulo n", text_color="red")

class Frame_ternas_Diofanto_2(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO DE DIOFANTO PARA ENCONTRAR TERNAS CON [P] Y [Q]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # TEXTO (p)
        self.texto1 = ctk.CTkLabel(
            self,
            text="[p]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto1.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

         # TEXTO (q)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[q]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=1, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto3 = ctk.CTkLabel(
            self,
            text="[n]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto3.grid(row=1, column=2, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (p)
        self.entry_p = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_p.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (q)
        self.entry_q = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_q.grid(row=2, column=1, padx=(5,5), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=2, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=3, pady=5)

    def calcular(self):
        try:
            p = int(self.entry_p.get())
            q = int(self.entry_q.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            x, y, z = MSED.ternas_Diofanto2(p, q, n)
            respuesta = f" [{x}]\u00B2 + [{y}]\u00B2 = [{z}]\u00B2 "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clases de equivalencia modulo n", text_color="red")

class Frame_ternas_Diofanto(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.seleccion = ctk.CTkSegmentedButton(
            self,
            values=["[m]", "[p] y [q]"],
            font=("Segoe UI", 13, "bold"),
            command=self.mostrar_vista)
        self.seleccion.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

         # Frame de Contenido
        self.c = ctk.CTkFrame(self, fg_color="gray20")
        self.c.grid(row=1, column=0, padx=(5,10), pady=10, sticky="nsew")

        self.v = {}
        self.v["[m]"] = Frame_ternas_Diofanto_1(self.c)
        self.v["[p] y [q]"] = Frame_ternas_Diofanto_2(self.c)
        
        for panel in self.v.values():
            panel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def mostrar_vista(self, nombre):
        if nombre in self.v:
            self.v[nombre].tkraise()

class Frame_ternas_Fibonacci(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # TITULO
        self.texto = ctk.CTkLabel(
            self,
            text="METODO CON LA SUCESIÓN DE FIBONACCI PARA ENCONTRAR TERNAS",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # TEXTO (m)
        self.texto1 = ctk.CTkLabel(
            self,
            text="[m]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto1.grid(row=1, column=0, padx=0, pady=1, sticky="ew")

        # TEXTO (n)
        self.texto2 = ctk.CTkLabel(
            self,
            text="[n]",
            fg_color="transparent",
            font=("Segoe UI", 13, "bold"),
        )
        self.texto2.grid(row=1, column=1, padx=0, pady=1, sticky="ew")
        
        ## Convertir la función de Python en una función que Tkinter entiende
        vcmd = (self.register(validar_numeros), '%P')

        # Entrada (m)
        self.entry_m = ctk.CTkEntry(
            self,
            placeholder_text ="25",
            validate="key",        
            validatecommand=vcmd)
        self.entry_m.grid(row=2, column=0, padx=(10,5), pady=10, sticky="ew")

        # Entrada (n)
        self.entry_n = ctk.CTkEntry(
            self,
            placeholder_text="100",
            validate="key",        
            validatecommand=vcmd)
        self.entry_n.grid(row=2, column=1, padx=(5,10), pady=10, sticky="ew")

        # Botón Calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="Calcular",
            command=self.calcular)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Texto Respuesta
        self.resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Segoe UI", 16, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            m = int(self.entry_m.get())
            n = int(self.entry_n.get())
            if (n<=0):
                self.resultado.configure(text="Error: n debe ser mayor que 0", text_color="red")
                return
            x, y, z = MSED.ternas_fibonacci(m, n)
            respuesta = f" [{x}]\u00B2 + [{y}]\u00B2 = [{z}]\u00B2 "
            self.resultado.configure(text=respuesta, text_color="#5fb3b3")
        except ValueError:
            self.resultado.configure(text="Error: Ingrese clase de equivalencia modulo n", text_color="red")

class Frame_superior(ctk.CTkFrame):

    def __init__(self, master, comando_menu, comando_inicio, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="gray20")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ruta_base = os.path.dirname(os.path.abspath(__file__))
        img_der_pil = Image.open(os.path.join(ruta_base, "..", "assets", "menu.ico"))
        self.imagen_menu = ctk.CTkImage(light_image=img_der_pil, size=(40,40))

        self.btn_menu = ctk.CTkButton(
            self, 
            image=self.imagen_menu,
            text="", 
            width=60,
            height=60,
            fg_color="transparent", 
            hover_color="gray20",
            command=comando_menu 
        )
        self.btn_menu.grid(row=0, column=0, padx=10, sticky="w")

        ruta_base = os.path.dirname(os.path.abspath(__file__))
        img_der_pil = Image.open(os.path.join(ruta_base, "..", "assets", "logo.ico"))
        self.imagen = ctk.CTkImage(light_image=img_der_pil, size=(60,60))

        self.btn_inicio = ctk.CTkButton(
            self,
            image=self.imagen,
            text="",
            width=60,
            height=60,
            fg_color="transparent", 
            hover_color="gray20",
            command=comando_inicio
            )
        self.btn_inicio.grid(row=0, column=1, padx=5, pady=(2,2), sticky="e")

class Frame_inicio(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.texto = ctk.CTkLabel(
            self,
            text="Una herramienta interactiva para el estudio de la divisibilidad y métodos de resolución de ecuaciones diofánticas en \u2124\u2099.",
            wraplength=500,
            justify="center",
            fg_color="transparent",
            font=("Times New Roman", 25, "italic")
        )
        self.texto.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ruta_base = os.path.dirname(os.path.abspath(__file__))
        img_der_pil = Image.open(os.path.join(ruta_base, "..", "assets", "inicio.png"))
        self.imagen = ctk.CTkImage(light_image=img_der_pil, size=(250,220))

        self.label = ctk.CTkLabel(
            self,
            image=self.imagen,
            text=""
            )
        self.label.grid(row=1, column=0, padx=5, pady=(2,2), sticky="ew")

        self.texto = ctk.CTkLabel(
            self,
            text="Frayban Mantilla \n Universidad de Pamplona \n 2026",
            fg_color="transparent",
            font=("Times New Roman", 18, "italic")
        )
        self.texto.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.menu_visible = True

        self.configure(fg_color="gray15")
        self.geometry("1000x500") # Tamaño de la ventana
        self.title("") # Titulo de la ventana
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "logo.ico")
        self.iconbitmap(icon_path) # Icono de la ventana

        # Configuración de columnas
        self.grid_columnconfigure(0, weight=1, minsize=340)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(1, weight=1)

        # Frame superior
        self.superior = Frame_superior(master=self, comando_menu=self.toggle_frame1, comando_inicio=self.mostrar_inicio, fg_color="gray20")
        self.superior.grid(row=0, column=0, columnspan=2, padx=10, pady=(5,0), sticky="nsew")

        # Frame de Menú
        self.menu_frame = Frame1(master=self,  fg_color="gray20", comando_cambio=self.mostrar_vista)
        self.menu_frame.grid(row=1, column=0, padx=(10,5), pady=5, sticky="nsew")
        
        # Frame de Contenido
        self.contenido = ctk.CTkFrame(self, fg_color="gray20")
        self.contenido.grid(row=1, column=1, padx=(5,10), pady=5, sticky="nsew")

        self.vistas = {}
        self.vistas["Algoritmo de la División"] = Frame_Algoritmo_Division(self.contenido)
        self.vistas["Algoritmo de Euclides"] = Frame_Algoritmo_Euclides(self.contenido)
        self.vistas["Maxímo Común Divisor"] = Frame_Maximo_Comun_Divisor(self.contenido)
        self.vistas["Lema de Bezout"] = Frame_Lema_Bezout(self.contenido)
        self.vistas["Algoritmo de la División en \u2124\u2099"] = Frame_Algoritmo_Division_zn(self.contenido)
        self.vistas["Algoritmo de Euclides en \u2124\u2099"] = Frame_Algoritmo_Euclides_zn(self.contenido)
        self.vistas["Maxímo Común Divisor en \u2124\u2099"] = Frame_Maximo_Comun_Divisor_zn(self.contenido)
        self.vistas["Lema de Bezout en \u2124\u2099"] = Frame_Lema_Bezout_zn(self.contenido)
        self.vistas["Metodo de la Falsa Posición"] = Frame_Falsa_Posicion(self.contenido)
        self.vistas["Metodo del Algoritmo de Euclides y Lema de Bezout"] = Frame_Euclides_Bezout(self.contenido)
        self.vistas["Metodo de Diofanto"] = Frame_Diofanto(self.contenido)
        self.vistas["Ternas con el Metodo de Diofanto"] = Frame_ternas_Diofanto(self.contenido)
        self.vistas["Metodo de Fibonacci"] = Frame_ternas_Fibonacci(self.contenido)
        self.vistas["Inicio"] = Frame_inicio(self.contenido)

        for panel in self.vistas.values():
            panel.place(relx=0, rely=0, relwidth=1, relheight=1)

    def mostrar_vista(self, nombre):
        if nombre in self.vistas:
            self.vistas[nombre].tkraise()

    def mostrar_inicio(self):
        self.mostrar_vista("Inicio")
    
    def toggle_frame1(self):
        if self.menu_visible:
            # Ocultamos el frame del menú
            self.menu_frame.grid_forget()
            # Hacemos que la columna 0 no ocupe espacio y la 1 se expanda
            self.grid_columnconfigure(0, weight=0, minsize=0)
            self.grid_columnconfigure(1, weight=1)
        else:
            # Volvemos a colocar el menú en su sitio original
            self.menu_frame.grid(row=1, column=0, padx=(10,5), pady=5, sticky="nsew")
            # Restauramos el peso y el tamaño mínimo de la columna del menú
            self.grid_columnconfigure(0, weight=1, minsize=340)
            self.grid_columnconfigure(1, weight=4)
        
        self.menu_visible = not self.menu_visible

fix_taskbar_icon()
app = App()
app.mainloop()
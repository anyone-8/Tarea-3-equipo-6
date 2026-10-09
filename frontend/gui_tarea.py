#gui de la tarea

from backend.crud_tarea import crud #type: ignore
import customtkinter as ctk
from PIL import Image

class gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.crud_t = crud()

        self._parametro_sp = False
        self._parametro_ap = False
        self._parametro_ep = False
        self._parametro_buscar = False

        self.geometry("1500x1000")
        self.title("administrador de personajes")
        self.menu_principal()

    def menu_principal(self):
        if self._parametro_sp == True:
            self.ocultar_seleccionar_personaje()
        if self._parametro_ap == True:
            self.ocultar_añadir_personaje()
        if self._parametro_buscar == True:
            self.ocultar_menu()

        

        self._m_principal = {}
        self._m_principal["place"] = {}
        e_place = self._m_principal["place"] 


        self._m_principal["front"] = ctk.CTkFont(family="consolas", size=22, weight="bold")
        self._m_principal["variable"] = ctk.StringVar()
        self._m_principal["variable"].trace_add("write", self.buscar_orden)

        e_place["menu_personajes"] = ctk.CTkScrollableFrame(self, width=1000, height=500)
        #e_place["opciones_busqueda"] = ctk.CTkOptionMenu(self, values=["por orden", "por nombre", "por categoria"], command=lambda choice: self.opciones_buscar(choice))
        e_place["titulo"] = ctk.CTkLabel(self, text="Personajes", font=self._m_principal["front"])
        e_place["buscador"] = ctk.CTkEntry(self, width=300, height=30)
        e_place["añadir"] = ctk.CTkButton(self, text="añadir personaje", width=100, height=30, command=self.menu_añadir_personaje)

        e_place["menu_personajes"].place(relx=0.5, rely=0.5, anchor="center")
        e_place["titulo"].place(relx=0.5, rely=0.04, anchor="center")
        e_place["buscador"].place(relx=0.5, rely=0.1, anchor="center")
        e_place["añadir"].place(relx=0.7, rely=0.1, anchor="center")
        #e_place["opciones_busqueda"].place(relx=0.3, rely=0.1, anchor="center")

        
        for elemento in self.crud_t.data.values():
            personaje_actual = elemento["nombre"]
            font2 = ctk.CTkFont(family="Helvetica", size=12, weight="bold")

            contenedores = ctk.CTkFrame(master=e_place["menu_personajes"], width=450, height=50, border_width=4, border_color="white")
            seleccionar = ctk.CTkButton(master=contenedores, text="", fg_color="transparent", width=420, height=40, command=lambda n=elemento: self.selccionar_personaje(n))
            nombre_personaje = ctk.CTkLabel(master=contenedores, text=personaje_actual, font=font2)
            imagen = Image.open(elemento["imagen"])
            imagen_final = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(30, 30))
            



            contenedores.pack(padx=0.2, pady=3)
            mostrar_imagen = ctk.CTkLabel(master=contenedores, image=imagen_final, text="")
            nombre_personaje.place(relx=0.3, rely=0.5, anchor="e")
            mostrar_imagen.place(relx=0.8, rely=0.5, anchor="e")
            seleccionar.place(relx=0.5, rely=0.5, anchor="center")
        

        self._parametro_sp = False
        self._parametro_ap = False
        self._parametro_buscar = False

    def selccionar_personaje(self, elemento):
        if self._parametro_ep == True:
            self.ocultar_editar_personaje()
            
        self.ocultar_menu()
        self._parametro_sp = True

        self._m_s_personaje = {}
        self._m_s_personaje["place"] = {}
        e_place = self._m_s_personaje["place"]

        imagen = Image.open(elemento["imagen"])
        font1 = ctk.CTkFont(family="consolas", size=26, weight="bold")

        imagen_final= ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(500, 500))
        e_place["mostrar_imagen"] = ctk.CTkLabel(self, image=imagen_final, text="")
        e_place["volver"] = ctk.CTkButton(self, text="volver", font=font1, width=100, height=30, command=self.menu_principal)
        e_place["nombre"] = ctk.CTkLabel(self, text=f"Nombre: {elemento["nombre"]}", font=font1)
        e_place["categorias"] = ctk.CTkLabel(self, text="Categoria:", font=font1)
        e_place["funcion"] = ctk.CTkLabel(self, text=f"-{elemento["categoria"]["funcion"]}", font=font1)
        e_place["rol"] = ctk.CTkLabel(self, text=f"-{elemento["categoria"]["rol"]}", font=font1)
        e_place["origen"] = ctk.CTkLabel(self, text=f"-{elemento["categoria"]["origen"]}", font=font1)
        e_place["caracteristicas"] = ctk.CTkLabel(self, text=elemento["caracteristicas"], font=font1, wraplength=500,fg_color="gray20", justify="left", corner_radius=6)
        e_place["editar"] = ctk.CTkButton(self, text="editar informacion", font=font1, width=200, height=30, command=lambda: self.menu_editar_personaje(elemento))
        e_place["borrar"] = ctk.CTkButton(self, text="borrar personaje", font=font1, width=200, height=30, fg_color="#8B0000", command=lambda: self.eliminar_personaje_gui(elemento))

        e_place["mostrar_imagen"].place(relx=0.05, rely=0.05, anchor="nw")
        e_place["nombre"].place(relx=0.5, rely=0.2, anchor="nw")
        e_place["categorias"].place(relx=0.5, rely=0.26, anchor="nw")
        e_place["funcion"].place(relx=0.55, rely=0.32, anchor="nw")
        e_place["rol"].place(relx=0.55, rely=0.38, anchor="nw")
        e_place["origen"].place(relx=0.55, rely=0.44, anchor="nw")
        e_place["volver"].place(relx=0.5, rely=0.15, anchor="nw")
        e_place["caracteristicas"].place(x=630, y=370, anchor="nw")
        e_place["editar"].place(relx=0.48, rely=0.8, anchor="nw")
        e_place["borrar"].place(relx=0.72, rely=0.8, anchor="nw")

        self._parametro_ep = False

    def menu_añadir_personaje(self):
        self.ocultar_menu()
        self._parametro_ap = True

        self._m_a_personaje = {}
        self._m_a_personaje["place"] = {}

        e_place = self._m_a_personaje["place"]

        font1 = ctk.CTkFont(family="consolas", size=16, weight="bold")
        font2 = ctk.CTkFont(family="helvetica", size=24, weight="bold")

        e_place["titulo"] = ctk.CTkLabel(self, text="Datos Del Personaje", font=font2)
        e_place["caja_nombre"] = ctk.CTkEntry(self, width=300, height=30)
        e_place["volver"] = ctk.CTkButton(self, text="volver", font=font1, width=100, height=30, command=self.menu_principal)
        e_place["nombre"] = ctk.CTkLabel(self, text="Nombre", font=font1)
        e_place["categoria"] = ctk.CTkLabel(self, text="categoria:", font=font1)
        e_place["funcion"] = ctk.CTkLabel(self, text="funcion-profesion", font=font1)
        e_place["caja_funcion"] = ctk.CTkEntry(self, width=300, height=30)
        e_place["rol"] = ctk.CTkLabel(self, text="rol", font=font1)
        e_place["caja_rol"] = ctk.CTkEntry(self, width=300, height=30)
        e_place["origen"] = ctk.CTkLabel(self, text="origen", font=font1)
        e_place["caja_origen"] = ctk.CTkEntry(self, width=300, height=30)
        e_place["caracteristicas"] = ctk.CTkLabel(self, text="carecteristicas", font=font1)
        e_place["caja_caracteristicas"] = ctk.CTkTextbox(self, width=300, height=150, activate_scrollbars=True)
        e_place["subir"] = ctk.CTkButton(self, text="subir imagen", font=font1, width=200, height=50, command=self.subir_imagen)
        e_place["añadir"] = ctk.CTkButton(self, text="añadir", font=font1, width=200, height=50, command=self.añadir_personaje_gui)

        e_place["caja_nombre"].place(relx=0.2, rely=0.2, anchor="nw")
        e_place["volver"].place(relx=0.05, rely=0.05, anchor="nw")
        e_place["nombre"].place(relx=0.1, rely=0.2, anchor="nw")
        e_place["titulo"].place(relx=0.5, rely=0.1, anchor="center")
        e_place["categoria"].place(relx=0.1, rely=0.30, anchor="nw")
        e_place["funcion"].place(relx=0.05, rely=0.40, anchor="nw")
        e_place["caja_funcion"].place(relx=0.2, rely=0.40, anchor="nw")
        e_place["rol"].place(relx=0.05, rely=0.50, anchor="nw")
        e_place["caja_rol"].place(relx=0.2, rely=0.50, anchor="nw")
        e_place["origen"].place(relx=0.05, rely=0.60, anchor="nw")
        e_place["caja_origen"].place(relx=0.2, rely=0.60, anchor="nw")
        e_place["caracteristicas"].place(relx=0.05, rely=0.70, anchor="nw")
        e_place["caja_caracteristicas"].place(relx=0.2, rely=0.70, anchor="nw")
        e_place["subir"].place(relx=0.7, rely=0.60, anchor="nw")
        e_place["añadir"].place(relx=0.7, rely=0.7, anchor="nw")

    def menu_editar_personaje(self, elemento):
        self.ocultar_seleccionar_personaje()
        self._parametro_ep = True

        self._m_e_personaje = {}
        self._m_e_personaje["place"] = {}

        e_place = self._m_e_personaje["place"]

        self._m_e_personaje["opciones"] = ctk.CTkOptionMenu(self, values=["nombre", "categoria", "caracteristicas", "imagen"], command=lambda choice: self.opciones_editar(choice, elemento))
        e_place["elemento_nulo"] = ctk.CTkLabel(self, text="codigo con funcion unica de no tener vacio el diccionario", width=1, height=1)
        self._m_e_personaje["regresar"] = ctk.CTkButton(self, text="volver", width=100, height=30, command=lambda: self.selccionar_personaje(elemento))

        self._m_e_personaje["opciones"].place(relx=0.5, rely=0.1, anchor="center")
        self._m_e_personaje["regresar"].place(relx=0.05, rely=0.05, anchor="nw")

        self._m_e_personaje["opciones"].set("nombre")

    def sub_menu_p_nombre(self):
        e_place = self._m_principal["place"]
        e_place["menu_personajes"].place_forget()
        e_place["buscador"].place_forget()

        self._m_principal["front"] = ctk.CTkFont(family="consolas", size=22, weight="bold")
        self._m_principal["variable"] = ctk.StringVar()
        self._m_principal["variable"].trace_add("write", self.buscar_nombre)

        e_place["buscador"] = ctk.CTkEntry(self, textvariable=self._m_principal["variable"], width=300, height=30)
        e_place["buscador"].place(relx=0.5, rely=0.1, anchor="center")



        


    def sub_menu_p_categoria(self):
        e_place = self._m_principal["place"]
        e_place["menu_personajes"].place_forget()
        e_place["buscador"].place_forget()

        e_place["m_p_nombre"] = ctk.CTkScrollableFrame(self, width=1000, height=500)
        e_place["m_p_nombre"].place(relx=0.5, rely=0.5, anchor="center")

        e_place["buscador"] = ctk.CTkEntry(self, textvariable=self._m_principal["variable"], width=300, height=30)
        e_place["buscador"].place(relx=0.5, rely=0.1, anchor="center")


    def ocultar_menu(self):
        for elemento in self._m_principal["place"].values():
            elemento.place_forget()

    def ocultar_seleccionar_personaje(self):
        for elemento in self._m_s_personaje["place"].values():
            elemento.place_forget()

    def ocultar_añadir_personaje(self):
        for elemento in self._m_a_personaje["place"].values():
            elemento.place_forget()

    def ocultar_editar_personaje(self):
        self._m_e_personaje["opciones"].place_forget()
        self._m_e_personaje["regresar"].place_forget()
        for personaje in self._m_e_personaje["place"].values():
            personaje.place_forget()

    def ocultar_opcion_editar_personaje(self):
        for elemento in self._m_e_personaje["place"].values():
            elemento.place_forget()

    def subir_imagen(self):
        self._archivo = ctk.filedialog.askopenfilename(title="selecciona una iamgen", filetypes=[("Imagenes jpg", "*.jpg")])

        if self._archivo:
            imagen_subida = Image.open(self._archivo)
            imagen_final = ctk.CTkImage(light_image=imagen_subida, dark_image=imagen_subida, size=(200, 200))
            self._m_a_personaje["place"]["mostrar_imagen"] = ctk.CTkLabel(self, image=imagen_final, text="")

            self._m_a_personaje["place"]["mostrar_imagen"].place(relx=0.7, rely=0.3, anchor="nw")

            if self._parametro_ep == True:
                self._m_e_personaje["place"]["mostrar_imagen"] = self._m_a_personaje["place"]["mostrar_imagen"]

    def añadir_personaje_gui(self):
        e_place = self._m_a_personaje["place"]

        nombre = e_place["caja_nombre"].get()
        funcion = e_place["caja_funcion"].get()
        rol = e_place["caja_rol"].get()
        origen = e_place["caja_origen"].get()
        caracteristicas = e_place["caja_caracteristicas"].get("1.0", "end")

        variable = self.crud_t.añadir_personaje(nombre, funcion, rol, origen, caracteristicas, self._archivo)

        if variable != None:
            self._m_a_personaje["place"]["error"] = ctk.CTkLabel(self, text=variable)

            self._m_a_personaje["place"]["error"].place(relx=0.7, rely=0.2, anchor="nw")

    def eliminar_personaje_gui(self, elemento):
        self.confirmar = ctk.CTkToplevel(self)
        self.confirmar.geometry("300x150")

        self.confirmar.focus_set()
        self.confirmar.grab_set()

        texto = ctk.CTkLabel(self.confirmar, text=f"¿Desea eliminar el personaje de {elemento["nombre"]}?")
        boton_si = ctk.CTkButton(self.confirmar, text="si", width=50, height=30, command=lambda: self.opcion_confirmar(1, elemento))
        boton_no = ctk.CTkButton(self.confirmar, text="no", width=50, height=30, command=lambda: self.opcion_confirmar(0, elemento))

        boton_si.place(relx=0.7, rely=0.7, anchor="nw")
        boton_no.place(relx=0.2, rely=0.7, anchor="nw")
        texto.place(relx=0.5, rely=0.2, anchor="center")

    def opcion_confirmar(self, bin, elemento):
        if bin == 0:
            self.confirmar.destroy()
        elif bin == 1:
            self.crud_t.eliminar_personaje(elemento)
            self.confirmar.destroy()
            self.menu_principal()

    def opciones_editar(self, opcion, elemento):
        e_place = self._m_e_personaje["place"]
        font1 = ctk.CTkFont(family="consolas", size=26, weight="bold")
        font2 = ctk.CTkFont(family="consolas", size=18, weight="bold")

        if opcion == "nombre":
            self.ocultar_opcion_editar_personaje()

            e_place["nombre_uso"] = ctk.CTkLabel(self, text=f"{elemento["nombre"]}", width=300, height=30, font=font1)
            e_place["nombre_nuevo"] = ctk.CTkEntry(self, width=300, height=30)
            e_place["nombre"] = ctk.CTkLabel(self, text="nombre actual", width=300, height=30, font=font1)
            e_place["nombre_nuevo_label"] = ctk.CTkLabel(self, text="nuevo nombre", width=300, height=30, font=font1)
            e_place["confirmar"] = ctk.CTkButton(self, text="aceptar", width=300, height=30, font=font1, command=lambda: self.editar_nombre_gui(elemento, opcion))

            e_place["nombre_uso"].place(relx=0.1, rely=0.5, anchor="nw")
            e_place["nombre_nuevo"].place(relx=0.55, rely=0.5, anchor="nw")
            e_place["nombre"].place(relx=0.1, rely=0.4, anchor="nw")
            e_place["nombre_nuevo_label"].place(relx=0.55, rely=0.4, anchor="nw")
            e_place["confirmar"].place(relx=0.55, rely=0.6, anchor="nw")

        if opcion == "categoria":
            self.ocultar_opcion_editar_personaje()

            e_place["categoria"] = ctk.CTkLabel(self, text="categoria", width=200, height=30, font=font2)
            e_place["funcion"] = ctk.CTkLabel(self, text="funcion", width=200, height=30, font=font2)
            e_place["rol"] = ctk.CTkLabel(self, text="rol", width=200, height=30, font=font2)
            e_place["origen"] = ctk.CTkLabel(self, text="origen", width=200, height=30, font=font2)

            e_place["funcion_uso"] = ctk.CTkLabel(self, text=elemento["categoria"]["funcion"], width=200, height=30, font=font2)
            e_place["rol_uso"] = ctk.CTkLabel(self, text=elemento["categoria"]["rol"], width=200, height=30, font=font2)
            e_place["origen_uso"] = ctk.CTkLabel(self, text=elemento["categoria"]["origen"], width=200, height=30, font=font2)

            e_place["caja_funcion"] = ctk.CTkEntry(self, width=200, height=30)
            e_place["caja_rol"] = ctk.CTkEntry(self, width=200, height=30)
            e_place["caja_origen"] = ctk.CTkEntry(self, width=200, height=30)

            e_place["aceptar"] = ctk.CTkButton(self, text="aceptar", width=300, height=30, font=font2, command=lambda: self.editar_categoria_gui(elemento, opcion))

            e_place["categoria"].place(relx=0.5, rely=0.3, anchor="center")
            e_place["funcion"].place(relx=0.2, rely=0.4, anchor="nw")
            e_place["rol"].place(relx=0.2, rely=0.5, anchor="nw")
            e_place["origen"].place(relx=0.2, rely=0.6, anchor="nw")

            e_place["funcion_uso"].place(relx=0.4, rely=0.4, anchor="nw")
            e_place["rol_uso"].place(relx=0.4, rely=0.5, anchor="nw")
            e_place["origen_uso"].place(relx=0.4, rely=0.6, anchor="nw")

            e_place["caja_funcion"].place(relx=0.7, rely=0.4, anchor="nw")
            e_place["caja_rol"].place(relx=0.7, rely=0.5, anchor="nw")
            e_place["caja_origen"].place(relx=0.7, rely=0.6, anchor="nw")

            e_place["aceptar"].place(relx=0.5, rely=0.7, anchor="center")

        if opcion == "caracteristicas":
            self.ocultar_opcion_editar_personaje()

            e_place["caracteristicas"] = ctk.CTkLabel(self, text="caracteristicas en uso", font=font1)
            e_place["caracteristicas_uso"] = ctk.CTkTextbox(self, width=300, height=100, activate_scrollbars=True)
            e_place["caracteristicas_nuevas"] = ctk.CTkLabel(self, text="caracteristicas nuevas", font=font1)
            e_place["caja_caracteristicas"] = ctk.CTkTextbox(self, width=300, height=100, activate_scrollbars=True)
            e_place["cambiar"] = ctk.CTkButton(self, text="cambiar", width=300, height=30, font=font2, command=lambda: self.editar_caracteristicas_gui(elemento, opcion))

            e_place["caracteristicas_uso"].configure(state="normal")
            e_place["caracteristicas_uso"].insert("1.0", elemento["caracteristicas"])
            e_place["caracteristicas_uso"].configure(state="disable")

            e_place["caracteristicas"].place(relx=0.23, rely=0.20, anchor="nw")
            e_place["caracteristicas_uso"].place(relx=0.23, rely=0.3, anchor="nw")
            e_place["caracteristicas_nuevas"].place(relx=0.53, rely=0.20, anchor="nw")
            e_place["caja_caracteristicas"].place(relx=0.53, rely=0.3, anchor="nw")
            e_place["cambiar"].place(relx=0.5, rely=0.6, anchor="center")

        if opcion == "imagen":
            self.ocultar_opcion_editar_personaje()
            self._m_a_personaje = {}
            self._m_a_personaje["place"] = {}
            

            imagen1 = Image.open(elemento["imagen"])
            imagen_final1 = ctk.CTkImage(light_image=imagen1, dark_image=imagen1, size=(200, 200))

            e_place["imagen"] = ctk.CTkLabel(self, text="imagen en uso", font=font1)
            e_place["imagen_uso"] = ctk.CTkLabel(self, image=imagen_final1, text="")
            e_place["imagen_nuevo"] = ctk.CTkLabel(self, text="nueva imagen", font=font1)
            e_place["subir"] = ctk.CTkButton(self, text="subir imagen", font=font2, command=self.subir_imagen)
            e_place["editar"] = ctk.CTkButton(self, text="editar", font=font2, command=lambda: self.editar_imagen_gui(elemento, opcion))

            e_place["imagen"].place(relx=0.15, rely=0.2, anchor="nw")
            e_place["imagen_uso"].place(relx=0.15, rely=0.3, anchor="nw")
            e_place["imagen_nuevo"].place(relx=0.7, rely=0.2, anchor="nw")
            e_place["subir"].place(relx=0.72, rely=0.65, anchor="nw")
            e_place["editar"].place(relx=0.72, rely=0.75, anchor="nw")

    def editar_nombre_gui(self, elemento, opcion):
        font1 = ctk.CTkFont(family="consolas", size=16, weight="bold")

        nombre = self._m_e_personaje["place"]["nombre_nuevo"].get()

        resultado =self.crud_t.editar_nombre(elemento, opcion, nombre)

        self._m_e_personaje["place"]["aceptado"] = ctk.CTkLabel(self, text=resultado, font=font1)

        self._m_e_personaje["place"]["aceptado"].place(relx=0.57, rely=0.2, anchor="nw")

    def editar_categoria_gui(self, elemento, opcion):
        funcion = self._m_e_personaje["place"]["caja_funcion"].get()
        rol = self._m_e_personaje["place"]["caja_rol"].get()
        origen = self._m_e_personaje["place"]["caja_origen"].get()

        self.crud_t.editar_categoria(elemento, opcion, funcion, rol, origen)

    def editar_caracteristicas_gui(self, elemento, opcion):
        caracteristicas = self._m_e_personaje["place"]["caja_caracteristicas"].get("1.0", "end")

        self.crud_t.editar_caracteristicas(elemento, opcion, caracteristicas)

    def editar_imagen_gui(self, elemento, opcion):
        imagen = self._archivo

        self.crud_t.editar_imagen(elemento, opcion, imagen)

    def opciones_buscar(self, opcion):
        self._parametro_buscar = True
        if opcion == "por orden":
            self.menu_principal()
        elif opcion == "por nombre":
            self.sub_menu_p_nombre()
        elif opcion == "por categoria":
            self.sub_menu_p_categoria()

    def buscar_orden(self, *args):

        texto = self._m_principal["place"]["buscador"].get().lower().replace(" ", "")

        if "menu_personajes" in self._m_principal["place"]:
            self._m_principal["place"]["menu_personajes"].place_forget()

        self._m_principal["front"] = ctk.CTkFont(family="consolas", size=22, weight="bold")
        #self._m_principal["variable"] = ctk.StringVar()
        self._m_principal["variable"].trace_add("write", self.buscar_orden)

        self._m_principal["place"]["menu_personajes"].place_forget()

        self._m_principal["place"]["m_p_nombre"] = ctk.CTkScrollableFrame(self, width=1000, height=500)

        self._m_principal["place"]["m_p_nombre"].place(relx=0.5, rely=0.5, anchor="center")





        if texto != "":
            for clave, elemento in self.crud_t.data.items():
                if texto in clave.lower().replace("-", ""):
                    personaje_actual = elemento["nombre"]
                    font2 = ctk.CTkFont(family="Helvetica", size=12, weight="bold")
                    
                    contenedores = ctk.CTkFrame(master=self._m_principal["place"]["m_p_nombre"], width=450, height=50, border_width=4, border_color="white")
                    seleccionar = ctk.CTkButton(master=contenedores, text="", fg_color="transparent", width=420, height=40, command=lambda n=elemento: self.selccionar_personaje(n))
                    nombre_personaje = ctk.CTkLabel(master=contenedores, text=personaje_actual, font=font2)
                    imagen = Image.open(elemento["imagen"])
                    imagen_final = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(30, 30))

                    contenedores.pack(padx=0.2, pady=3)
                    mostrar_imagen = ctk.CTkLabel(master=contenedores, image=imagen_final, text="")
                    nombre_personaje.place(relx=0.3, rely=0.5, anchor="e")
                    mostrar_imagen.place(relx=0.8, rely=0.5, anchor="e")
                    seleccionar.place(relx=0.5, rely=0.5, anchor="center")
        elif texto == "":
            for elemento in self.crud_t.data.values():
                personaje_actual = elemento["nombre"]
                font2 = ctk.CTkFont(family="Helvetica", size=12, weight="bold")
            
                contenedores = ctk.CTkFrame(master=self._m_principal["place"]["m_p_nombre"], width=450, height=50, border_width=4, border_color="white")
                seleccionar = ctk.CTkButton(master=contenedores, text="", fg_color="transparent", width=420, height=40, command=lambda n=elemento: self.selccionar_personaje(n))
                nombre_personaje = ctk.CTkLabel(master=contenedores, text=personaje_actual, font=font2)
                imagen = Image.open(elemento["imagen"])
                imagen_final = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(30, 30))
                        
            
            
            
                contenedores.pack(padx=0.2, pady=3)
                mostrar_imagen = ctk.CTkLabel(master=contenedores, image=imagen_final, text="")
                nombre_personaje.place(relx=0.3, rely=0.5, anchor="e")
                mostrar_imagen.place(relx=0.8, rely=0.5, anchor="e")
                seleccionar.place(relx=0.5, rely=0.5, anchor="center")
            
    def buscar_nombre(self, *args):
        e_place = self._m_principal["place"]

        

        texto = self._m_principal["place"]["buscador"].get().lower().replace(" ", "")
        e_place["m_p_nombre"] = ctk.CTkScrollableFrame(self, width=1000, height=500)
        e_place["m_p_nombre"].place(relx=0.5, rely=0.5, anchor="center")

        if texto:
            for elemento in self.crud_t.data.values():
                if texto in elemento["nombre"].lower().replace("-", ""):
                    personaje_actual = elemento["nombre"]
                    font2 = ctk.CTkFont(family="Helvetica", size=12, weight="bold")
                                    
                    contenedores = ctk.CTkFrame(master=e_place["m_p_nombre"], width=450, height=50, border_width=4, border_color="white")
                    seleccionar = ctk.CTkButton(master=contenedores, text="", fg_color="transparent", width=420, height=40, command=lambda n=elemento: self.selccionar_personaje(n))
                    nombre_personaje = ctk.CTkLabel(master=contenedores, text=personaje_actual, font=font2)
                    imagen = Image.open(elemento["imagen"])
                    imagen_final = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(30, 30))
                
                    contenedores.pack(padx=0.2, pady=3)
                    mostrar_imagen = ctk.CTkLabel(master=contenedores, image=imagen_final, text="")
                    nombre_personaje.place(relx=0.3, rely=0.5, anchor="e")
                    mostrar_imagen.place(relx=0.8, rely=0.5, anchor="e")
                    seleccionar.place(relx=0.5, rely=0.5, anchor="center")      

    def buscar_categoria(self, *args):
        e_place = self._m_principal["place"]

        if "menu_personajes" in e_place:
            e_place["menu_personajes"].place_forget()

        texto = e_place["buscador"].get().lower().replace(" ", "")
        e_place["m_p_nombre"] = ctk.CTkScrollableFrame(self, width=1000, height=500)
        e_place["m_p_nombre"].place(relx=0.5, rely=0.5, anchor="center")

        if texto:
            for elemento in self.crud_t.data.values():
                if any(texto.lower().replace(" ", "") in str(valor_texto).lower().replace(" ", "") for valor_texto in elemento["categoria"].values()):
                    personaje_actual = elemento["nombre"]
                    font2 = ctk.CTkFont(family="Helvetica", size=12, weight="bold")
                                    
                    contenedores = ctk.CTkFrame(master=e_place["m_p_nombre"], width=450, height=50, border_width=4, border_color="white")
                    seleccionar = ctk.CTkButton(master=contenedores, text="", fg_color="transparent", width=420, height=40, command=lambda n=elemento: self.selccionar_personaje(n))
                    nombre_personaje = ctk.CTkLabel(master=contenedores, text=personaje_actual, font=font2)
                    imagen = Image.open(elemento["imagen"])
                    imagen_final = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(30, 30))
                
                    contenedores.pack(padx=0.2, pady=3)
                    mostrar_imagen = ctk.CTkLabel(master=contenedores, image=imagen_final, text="")
                    nombre_personaje.place(relx=0.3, rely=0.5, anchor="e")
                    mostrar_imagen.place(relx=0.8, rely=0.5, anchor="e")
                    seleccionar.place(relx=0.5, rely=0.5, anchor="center") 
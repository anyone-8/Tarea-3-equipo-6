#backend de la tarea para el viernes
import json
import shutil
import os

class crud():
    def __init__(self, ruta="datos/data_tarea.json"):
        self.json = ruta
        self.data = self.cargar_json()

    def cargar_json(self):
        try:
            with open(self.json, "r", encoding="utf-8") as f:
                return json.load(f)
            #hacemos que el codigo no siga corriendo si es que no se encuentrea el json, hay que correjir
        except(FileNotFoundError, FileExistsError, PermissionError, json.JSONDecodeError) as e:
            raise RuntimeError(f"ERROR: No se pudo leer el json: {e}")

    def guardar(self):
        try:
            with open(self.json, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4)
            return True

        #Si de casualidad no se puede escribrir damos false para avisar que no se pudo}
        #relizar la accion
        except(FileExistsError, PermissionError, OSError):
            return False

    def añadir_personaje(self, nombre, funcion, rol, origen, caracteristicas, imagen):
        #comprobar si el personaje existe
        for personaje in self.data.values():
            if nombre.lower().replace(" ", "") in personaje["nombre"].lower().replace(" ", ""):
                return "Personaje ya existente"

        nombre = nombre.replace(" ", "_")

        contador = 1
        while f"personaje-{contador}" in self.data.keys():
            contador += 1

        clave = f"personaje-{contador}"

        nuevo_personaje = {
            clave : {
                "nombre" : f"{nombre}",
                "categoria" : {
                    "funcion" : f"{funcion}",
                    "rol" : f"{rol}",
                    "origen" : f"{origen}"
                },
                "caracteristicas" : f"{caracteristicas}",
                "imagen" : f"datos/imagenes/{nombre}.jpg"
            }
        }


        nombre_base_imagen = os.path.basename(imagen)
        nombre_puente = os.path.join(f"datos/imagenes/{nombre_base_imagen}")
        shutil.copy2(imagen, nombre_puente)
        os.rename(nombre_puente, nuevo_personaje[clave]["imagen"])

        self.data.update(nuevo_personaje)

        if self.guardar():
            return f"El personaje {nombre} se guardo con exito"
        else:
            self.data.pop(clave, None)
            os.remove(nuevo_personaje[clave]["imagen"])
            return f"El personaje {nombre} no se pudo añadir"

    def eliminar_personaje(self, elemento):
        for clave, personaje in self.data.items():
            if personaje["nombre"].lower().replace(" ", "_") == elemento["nombre"].lower().replace(" ", "_"):
                personaje_eliminado = self.data.pop(clave, None)
                break

        if self.guardar():
            os.remove(elemento["imagen"])
            return "el personaje se elimino con exito"

        else:
            self.data.update(personaje_eliminado)
            return "el personaje no se elimino"

    def editar_nombre(self, elemento, opcion, nombre):
        for clave, valor in self.data.items():
            if valor == elemento:
                nombre_antiguo = self.data[clave][opcion]
                imagen_antigua = self.data[clave]["imagen"]
                self.data[clave][opcion] = nombre.replace(" ", "_")
                nueva_imagen = f"datos/imagenes/{nombre.replace(" ", "_")}.jpg"
                self.data[clave]["imagen"] = nueva_imagen

        if self.guardar():
            os.rename(imagen_antigua, nueva_imagen)
            return "se guardo con exito el cambio"
        else:
            self.data[clave][opcion] = nombre_antiguo
            self.data[clave]["imagen"] = imagen_antigua
            return "no se guardo el cambio"

    def editar_categoria(self, elemento, opcion, funcion, rol, origen):
        for clave, valor in self.data.items():
            if valor == elemento:
                funcion_antigua = self.data[clave][opcion]["funcion"]
                rol_antiguo = self.data[clave][opcion]["rol"]
                origen_antiguo = self.data[clave][opcion]["origen"]

                

                break

        self.data[clave][opcion]["funcion"] = funcion
        self.data[clave][opcion]["rol"] = rol
        self.data[clave][opcion]["origen"] = origen

        if self.guardar():
            return "Los cambios se hicieron con exito"
        else:
            self.data[clave][opcion]["funcion"] = funcion_antigua
            self.data[clave][opcion]["rol"] = rol_antiguo
            self.data[clave][opcion]["origen"] = origen_antiguo
            return "No se pudieron realizar los cambios"
        

    def editar_caracteristicas(self, elemento, opcion, caracteristicas):
        for clave, valor in self.data.items():
            if valor == elemento:
                caracteristicas_antiguas = self.data[clave][opcion]
                break

        self.data[clave][opcion] = caracteristicas

        if self.guardar():
            return "El cambio se guardo con exito"
        else:
            self.data[clave][opcion] = caracteristicas_antiguas
            return "No se pudo guardar el cambio"

    def editar_imagen(self, elemento, opcion, imagen):
        for clave, valor in self.data.items():
            if valor == elemento:
                imagen_antigua = self.data[clave][opcion]
                break

        if self.guardar():
            shutil.copy2(imagen, imagen_antigua)

            return "Imagen guardada con exito"
        else:
            return "No se pudo guardar la imagen"

        
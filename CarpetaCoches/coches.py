from P2_POO.coches_system_Coches_Camiones.conexionBD import conexion, cursor
class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._plazas = plazas

    # Métodos de comportamiento
    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1
    @property
    def Velocidad(self):
        return self._velocidad

    @Velocidad.setter
    def Velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def Potencia(self):
        return self._potencia

    @Potencia.setter
    def Potencia(self, potencia):
        self._potencia = potencia

    @property
    def Plazas(self):
        return self._plazas

    @Plazas.setter
    def Plazas(self, plazas):
        self._plazas = plazas

    @property
    def Marca(self):
        return self._marca

    @Marca.setter
    def Marca(self, marca):
        self._marca = marca

    @property
    def Color(self):
        return self._color

    @Color.setter
    def Color(self, color):
        self._color = color

    @property
    def Modelo(self):
        return self._modelo

    @Modelo.setter
    def Modelo(self, modelo):
        self._modelo = modelo

    def insertar(self):
            try:
                cursor.execute(
                    "INSERT INTO coches VALUES (NULL, %s, %s, %s, %s, %s, %s)",
                    (self._marca, self._color, self._modelo,
                     self._velocidad, self._potencia, self._plazas)
                )
                conexion.commit()
                return True
            except Exception as e:
                print("Error al insertar:", e)  # <-- imprime el error real
                return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except Exception as e:
            print("Error al consultar:", e)
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print("Error al eliminar:", e)
            return False
    
    def actualizar(self, id):
            try:
                cursor.execute(
                    "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, plazas=%s WHERE id=%s",
                    (self._marca, self._color, self._modelo,
                     self._velocidad, self._potencia, self._plazas, id)
                )
                conexion.commit()
                return True
            except Exception as e:
                print("Error al actualizar:", e)
                return False
# Clase Camionetas (hereda de Coches)
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, plazas)
        self._traccion = traccion
        self._cerrada = cerrada

    def transportar(self, num_pasajeros):
        print(f"El número de pasajeros de la camioneta es: {num_pasajeros}")

    def acelerar(self):
        self._velocidad += 1
        print("Estoy acelerando como una camioneta")

    def frenar(self):
        self._velocidad -= 1
        print("Estoy desacelerando como una camioneta")

    @property
    def Traccion(self):
        return self._traccion

    Traccion.setter
    def Traccion(self, traccion):
            self._traccion = traccion
    
    @property
    def Cerrada(self):
        return self._cerrada

    Cerrada.setter
    def Cerrada(self, cerrada):
        self._cerrada = cerrada


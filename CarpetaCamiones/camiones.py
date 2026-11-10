from P2_POO.coches_system_Coches_Camiones.conexionBD import conexion,cursor
from P2_POO.coches_system_Coches_Camiones.CarpetaCoches import coches
class Camiones(coches.Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, plazas)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    def cargar(self, tipo_carga):
        print(f"El tipo de carga del camión es: {tipo_carga}")

    def acelerar(self):
        self._velocidad += 2
        print("Estoy acelerando como un camión")

    def frenar(self):
        self._velocidad -= 2
        print("Estoy desacelerando como un camión")

    def cargar(self,tipo_carga):
             print(f"la carga es de: {tipo_carga}")
             
    @property
    def Eje(self):
         return self._eje
  
    @Eje.setter
    def Eje(self, eje):
        self._eje = eje
    
    @property
    def CapacidadCarga(self):
        return self._capacidadCarga

    @CapacidadCarga.setter
    def CapacidadCarga(self, capacidadCarga):
        self._capacidadCarga = capacidadCarga

    def insertar(self):
            try:
                cursor.execute(
                    "INSERT INTO camiones VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self._marca, self._color, self._modelo, self._velocidad,
                     self._potencia, self._plazas, self._eje, self._capacidadCarga)
                )
                conexion.commit()
                return True
            except:
                return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except Exception as e:
            print("Error al consultar:", e)
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print("Error al eliminar:", e)
            return False

    
    def actualizar(self, id):
            try:
                cursor.execute(
                    "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id=%s",
                    (self._marca, self._color, self._modelo, self._velocidad,
                     self._potencia, self._plazas, self._eje, self._capacidadCarga, id)
                )
                conexion.commit()
                return True
            except:
                return False

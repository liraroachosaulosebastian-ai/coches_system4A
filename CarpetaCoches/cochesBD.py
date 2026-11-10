from P2_POO.coches_system_Coches_Camiones.conexionBD import conexion, cursor

class CochesBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._plazas = plazas

    # def insertar(self):
    #     try:
    #         cursor.execute(
    #             "INSERT INTO coches VALUES (NULL, %s, %s, %s, %s, %s, %s)",
    #             (self._marca, self._color, self._modelo,
    #              self._velocidad, self._potencia, self._plazas)
    #         )
    #         conexion.commit()
    #         return True
    #     except Exception as e:
    #         print("Error al insertar:", e)  # <-- imprime el error real
    #         return False

    # def consultar(self):
    #     try:
    #         cursor.execute("SELECT * FROM coches")
    #         return cursor.fetchall()
    #     except Exception as e:
    #         print("Error al consultar:", e)
    #         return []

    # def eliminar(self, id):
    #     try:
    #         cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
    #         conexion.commit()
    #         return True
    #     except Exception as e:
    #         print("Error al eliminar:", e)
    #         return False

    # def actualizar(self, id):
    #     try:
    #         cursor.execute(
    #             "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, plazas=%s WHERE id=%s",
    #             (self._marca, self._color, self._modelo,
    #              self._velocidad, self._potencia, self._plazas, id)
    #         )
    #         conexion.commit()
    #         return True
    #     except Exception as e:
    #         print("Error al actualizar:", e)
    #         return False

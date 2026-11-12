from tkinter import *
from tkinter import messagebox
from CarpetaCoches import coches,coches

class App:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(False, False)

        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def respuesta_sql(self, respuesta):

        if respuesta:
            messagebox.showinfo("Correcto","Acción realizada correctamente")

        else:
            messagebox.showerror("Error","Ocurrió un error en la operación")

    def main(self):

        self.borrarPantalla()

        Label(self.ventana,
            text="::: MENÚ PRINCIPAL :::",
            font=("Arial", 16)).pack(pady=20)

        Button(self.ventana,
            text="Coches",
            width=20,
            command=self.menu_acciones).pack(pady=10)

        Button(self.ventana,
            text="Salir",
            width=20,
            command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):

        self.borrarPantalla()

        Label(
            self.ventana,
            text="::: MENÚ DE COCHES :::",
            font=("Arial", 16)
        ).pack(pady=20)

        Button(
            self.ventana,
            text="Agregar",
            width=20,
            command=self.insertar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Eliminar",
            width=20,
            command=self.eliminar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Modificar",
            width=20,
            command=self.modificar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Consultar",
            width=20,
            command=self.consultar_view
        ).pack(pady=5)

        Button(
            self.ventana,
            text="Regresar",
            width=20,
            command=self.main
        ).pack(pady=5)

    def insertar_view(self):

        self.borrarPantalla()

        Label(self.ventana, text="Agregar coche").pack(pady=10)

        Label(self.ventana, text="Marca").pack()
        self.marca = Entry(self.ventana)
        self.marca.pack()

        Label(self.ventana, text="Color").pack()
        self.color = Entry(self.ventana)
        self.color.pack()

        Label(self.ventana, text="Modelo").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.pack()

        Label(self.ventana, text="Velocidad").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack()

        Label(self.ventana, text="Potencia").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.pack()

        Label(self.ventana, text="Plazas").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.pack()

        Button(
            self.ventana,
            text="Guardar",
            command=lambda: {self.insertar_controller(),self.insertar_view()}).pack(pady=10)

        Button(
            self.ventana,
            text="Regresar",
            command=self.menu_acciones
        ).pack()

    def insertar_controller(self):

        coche1 = coches.Coches(
            self.marca.get().upper(),
            self.color.get().upper(),
            self.modelo.get().upper(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )

        respuesta = coche1.insertar()

        self.respuesta_sql(respuesta)
    
    def eliminar_view(self):

        self.borrarPantalla()

        Label(self.ventana,
            text="Eliminar coche").pack(pady=10)

        Label(self.ventana, text="ID").pack()

        self.id = Entry(self.ventana)
        self.id.pack()

        self.btn_buscar=Button(self.ventana, text="Buscar",command=lambda:self.buscar_controler("Eliminar"))
        self.btn_buscar.pack(pady=5)
        
        self.btn_eliminar=Button(self.ventana,text="Eliminar",state="disabled",command=lambda: {self.eliminar_controller(), self.eliminar_view()})
        self.btn_eliminar.pack(pady=5)

        Button(self.ventana,
            text="Regresar",
            command=self.menu_acciones).pack()

    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
           respuesta = coches.Coches.eliminar(id)
        else:
            respuesta=False
            self.respuesta_sql(respuesta)

    def modificar_view(self):

        self.borrarPantalla()

        Label(self.ventana,
            text="Modificar coche").pack(pady=10)

        Label(self.ventana, text="ID").pack()
        self.id = Entry(self.ventana)
        self.id.pack()

        Label(self.ventana, text="Marca").pack()
        self.marca = Entry(self.ventana)
        self.marca.pack()

        Label(self.ventana, text="Color").pack()
        self.color = Entry(self.ventana)
        self.color.pack()

        Label(self.ventana, text="Modelo").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.pack()

        Label(self.ventana, text="Velocidad").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack()

        Label(self.ventana, text="Potencia").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.pack()

        Label(self.ventana, text="Plazas").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.pack()

        Button(self.ventana,
            text="Actualizar",
            command=lambda: {self.modificar_controller(), self.modificar_view()}).pack(pady=10)

        Button(self.ventana,
            text="Regresar",
            command=self.menu_acciones).pack()

    def modificar_controller(self):
        coche1 = coches.Coches(self.marca.get().upper(),self.color.get().upper(),self.modelo.get().upper(),self.velocidad.get(),self.potencia.get(),self.asientos.get())

        respuesta = coche1.actualizar(self.id.get())

        self.respuesta_sql(respuesta)

    def buscar_controler(self,tipo_accion):
        id=self.id.get()
        coche1=coches.Coches.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="..! Registro encontrado !...",menssage=f"...! El registro fue encontrado con exito, puedes {tipo_accion}!...")
            self.cambiar_estado_btn(True,tipo_accion)

        else:
            messagebox.showerror(title="..! Verifica por favor !...",menssage=f"...! El registro no fue encontrado, no es posoble {tipo_accion}!...")
            self.cambiar_estado_btn(False,tipo_accion)

    def cambiar_estado_btn(self, estado, tipo_accion):
        if estado:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="normal")
        else:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="disabled")
            
    def consultar_view(self):

        self.borrarPantalla()
        Label(self.ventana,text="Listado de coches",font=("Arial", 14)).pack(pady=10)
        registros = coches.Coches.consultar()
        texto = ""
        if registros:
            for fila in registros:
                texto += (
                    f"{'ID':<20}: {fila[0]:<20}\n"
                    f"{'Marca':<20}: {fila[1]:<20}\n"
                    f"{'Color':<20}: {fila[2]:<20}\n"
                    f"{'Modelo':<20}: {fila[3]:<20}\n"
                    f"{'Velocidad':<20}: {fila[4]:<20}\n"
                    f"{'Potencia':<20}: {fila[5]:<20}\n"
                    f"{'Plazas':20}: {fila[6]:<20}\n"
                    f"{'-'*30}\n")
        else:
            texto = "No existen registros."
        Label(self.ventana,
            text=texto,
            justify=LEFT).pack()
        Button(self.ventana,
            text="Regresar",
            command=self.menu_acciones).pack(pady=10)

    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...!Atencion!..",message=f"...¿Desea {tipo} este registro?...")
        if resp=="yes":
            return True
        else:
            return False
        
if __name__ == "__main__":

    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()



import pyodbc
server='SQL SERVER'
database = 'MiDatos'
user ='sa'
paswoord ='123456'

class Persona_datos():
    def __init__(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={SQL SERVER}; SERVER='+server+';DATABASE='+database+';USER='+user+'; PWD='+paswoord)
            print('conexion exitosa')
        except:
            print('conexion fallida')

    def agregar_datos(self,nombre,edad,correo,telefono):
        cursorIngresar = self.conexion.cursor() 
        consultar = "Insert into Datos_Person(Nombre,Edad,Correo,Telefono) values(?,?,?,?)"
        cursorIngresar.execute(consultar,(nombre,edad,correo,telefono))
        self.conexion.commit()
        cursorIngresar.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        mostrar = "Select * From Datos_Person"
        cursor.execute(mostrar)
        registros = cursor.fetchall()
        return registros

    def eliminar_datos(self,nombre):
        try:
            cursor = self.conexion.cursor()
            eliminar = "Delete From Datos_Person WHERE Nombre =?"
            print(f"Consulta a ejecutar: {eliminar} parametro:{nombre}")
            cursor.execute(eliminar,(nombre))
            self.conexion.commit()
            print("Registro eliminado exitosamente")
        except Exception as e:
            print(f"Error al eliminar datos: {e}")

        finally:
            cursor.close()
        

    def actulizar_datos(self,ID,nombre,edad,correo,telefono):
        try:
            cursor = self.conexion.cursor()
            actualizar = """UPDATE Datos_Person SET Nombre =?, Edad = ?, Correo = ?, Telefono = ?  WHERE ID=?"""
            
            print(f"consulta: {actualizar}")
            print(f"valores: {nombre},{edad},{telefono},{ID}")
            cursor.execute(actualizar,(nombre,edad,correo,telefono,ID))
            dato = cursor.rowcount
            self.conexion.commit()
            cursor.close()
            return dato
        except Exception as e:
            print(f"error al actulizar los datos: {e}")
           
    


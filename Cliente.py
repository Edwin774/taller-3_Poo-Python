# *****zona de clase *******
# se crea la clase
class cliente:
    # se crea el metodo constructo de la clase
    def _init_(self):
        # se crean los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
        
        # crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre
        
    def set_apellido(self, dato_apellido):
        self.set_apellido = dato_apellido
            
        # se crean metodos normales de la clase
        
    def tomar_datos(self):
        self.nombre_cliente = input("digite el nombre del cliente: ")
        self.apellido_cliente = input("digite el apellido del cliente: ")
           
    def procesar_datos(self):
        aux = self.nombre_cliente +" "+self.apellido_cliente
    
    def mostrar_info_cliente(self):
        print(f"nombre del cliente: {self.nombre_cliente} - apellido cliente: {self.apellido_cliente}")
        
    def hacer_saludo(self, datosaludo):
        print(f"{datosaludo} : {self.get_nombre}  {self.get_apellido}")
    
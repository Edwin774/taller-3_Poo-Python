from Cliente import cliente

class saludo:
    def _init_(self):
        self.obj_cliente = cliente()
        
    def hacer_saludo_formal(self):
        mensaje = "saludo formal: "
        return mensaje
    
    def hacer_despedida_formal(self):
        mensaje = "hasta luego formal"
        return mensaje
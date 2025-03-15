# ** codigo principal **
from Cliente import cliente
from saludo import saludo
#creo el objeto cliente
objcliente = cliente()
objsaludo = saludo()

objcliente.tomar_datos()
aux_mensaje = objsaludo.hacer_saludo_formal()
objcliente.hacer_saludo(aux_mensaje)
# llamo a los metodos del objeto


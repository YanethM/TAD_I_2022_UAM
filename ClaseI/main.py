#1. Importamos la clase
from saludo import Saludo
from lists import Lists

#2. Creamos la instancia de la clase
inst_saludo = Saludo()
inst_lists = Lists()

#3. Mediante la instancia llamamos las funciones, métodos o attri de la clase
inst_saludo.show_message()
inst_lists.show_list()
print('Función que añade una nueva mascota ', inst_lists.add_element())
inst_lists.delete_end_element()
inst_lists.delete_first_element()

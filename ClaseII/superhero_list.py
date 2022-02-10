# from colorama import Fore, init
# init()

class SuperheroList:
    #Método inicializador de la clase
    def __init__(self):
        #Creación de una lista vacía
        self.superhero_list = []
        self.length_list = 0
        self.superhero = ""
        
    def add_elements_to_list(self):
        #Consultar al user cuántos elementos desea añadir
        print("<<<<<<<<<<<<<<<<<<<<<LISTAS EN PYTHON>>>>>>>>>>>>>>>>>>>\n")
        
        #Entramos en un ciclo para validar si el user ingresa un num entero
        while True:
            try:
                #1. Recibir una entreda de un valor númerico por parte del user int(input(valor))
                self.length_list = int(input("¿Cuántos superheroes deseas añadir?\n         >>>"))
                #2. Creamos el ciclo for
                for i in range (0, self.length_list):
                    #3. Solicitamos el nombre de los superheroes
                    self.superhero = input("            >>> Superheroe: ")
                    #4. Añado el nombre del superheroe ingresado en la lista
                    self.superhero_list.append(self.superhero )
                #5. Imprimo la lista
                print(self.superhero_list)
                #6. Salir del ciclo while
                break
            #En caso de que el user no ingrese un valor entero, se muestra un msn de excepción
            except ValueError:
                # Se muestra mensaje de error, no se utiliza break
                print(">>>>>>>>>>>>>>>>>>>>El valor ingresado no es un número<<<<<<<<<<<<<<<<")
                
    def delete_elements(self):
        #Validar que el valor ingresado por el usuario sea un valor entero
        while True:
            try:
                option = int(input("                Seleccione la posición del superheroe a eliminar\n          1. El primero\n          2. El último\n          3. Por el nombre\n          >>>"))
                if option != 1 and option != 2 and option != 3:
                    option = int(input("             >>> Opción incorrecta <<<\n          >>>"))
                elif option == 1:
                    #El user ha seleccionado eliminar el primer superheroe
                    self.superhero_list.pop(0)
                    print(self.superhero_list)
                    break
                elif option == 2:
                    self.superhero_list.pop()
                    print(self.superhero_list)
                    break
                else:
                    self.superhero = input('                Ingresa el nombre del superheroe a eliminar\n          >>>')
                    for item in range(len(self.superhero_list)):
                        if self.superhero_list[item] == self.superhero:
                            while True:
                                try:
                                    option_delete = int(input(f"Confima desea eliminar el superheroe {self.superhero}?\n          1. Si\n          2. No\n          >>>"))
                                    if option_delete != 1 and option_delete != 2:
                                        break
                                    elif option_delete == 1:
                                        self.superhero_list.remove(self.superhero)
                                        print(self.superhero_list)
                                        break
                                    else:
                                        print(self.superhero_list)
                                        break
                                except ValueError:
                                    print("             >>> Se esperaba un valor númerico <<<")    
                            break                        
                    break
            except ValueError:
                print("             >>> Se esperaba un valor númerico <<<")
        
        
    def insert_element(self):
        self.superhero = input("            Ingresa el nombre del superheroe\n          >>>")
        while True:
            try:
                index = int(input("            Ingresa el indice\n          >>>"))
                if(index < 0 or index > len(self.superhero_list)):
                    index = int(input("            Indice fuera del rango\n          >>>"))
                else:
                    self.superhero_list.insert(index, self.superhero)
                    print(self.superhero_list)
                    break
            except ValueError:
                print("             >>> Se esperaba un valor númerico <<<")   
                
    def reverse_list(self):
        self.superhero_list.reverse()
        print(self.superhero_list)
             
                
                
                
    
    
            
            
                
            
    

    
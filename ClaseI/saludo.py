class Saludo:
    #Método inicializador de la clase
    def __init__(self):
        self.saludo = 'Hello world'
    
    #Método que imprime el valor de la variable global
    def show_message(self):
        print(f'Mostrar mensaje {self.saludo}')
        
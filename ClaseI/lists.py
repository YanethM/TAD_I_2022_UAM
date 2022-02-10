class Lists:
    def __init__(self):
        self.pets = ['dog', 'cat', 'fishes']
    
    def show_list(self):
        print(f'My pets are:\n{self.pets}')
        
    #Añadir elemento al final de la lista
    def add_element(self):
        self.pets.append('elephant')
        return self.pets
    
    #Eliminar el último elemento de la lista
    def delete_end_element(self):
        print(f'Se ha eliminado la mascota: {self.pets.pop()}')
    
    #Eliminar el primer elemento de la lista
    def delete_first_element(self):
        print(f'Se ha eliminado la mascota: {self.pets.pop(0)}')
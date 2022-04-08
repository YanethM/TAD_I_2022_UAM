class CircularLinkedList:
    ''' Le definimos la clase nodo '''
    class Node:
        def __init__(self, value):
            ''' Valor y nodo siguiente '''
            self.value = value
            self.next_node = None
    ''' Inicializamos la clase CircularLinkedList '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    '''Creamos la función encargada de imprimir la lista  '''
    def show_circular_linked_list(self):
        node_list = []
        current_node = self.head
        ''' Bandera para manejar el estado de true y false en el recorrido de la lista
        true = quiere decir que hay más nodos '''
        pivote = True
        cant_nodes_cll = self.length
        ''' Mientrs la cantidad de nodos sea diferente de cero, hay nodos por recorrer '''
        while cant_nodes_cll != 0:
            ''' Mientras el pivote sea True o el nodo actual visitado sea diferente a la cabeza
            Cuando el pivote vuelva a ser True y el nodo actual la cabeza finaliza el recorrido'''
            if pivote != False or current_node != self.head:
                ''' Añadimos el nodo a la lista vacía que es la que imprimimos '''
                node_list.append(current_node.value)
                ''' Incrementamos en una posición el nodo actual que estamos visitando '''
                current_node = current_node.next_node
                pivote = False
                ''' Disminuimos en 1 la longitud de la lista
                Quedando ya menos nodos por visitar '''
                cant_nodes_cll -= 1
            else:
                ''' Si es la cabeza de la lista finalizo recorrido porque ya se visito '''
                break
        print(node_list)
    


    ''' Método para añadir nodos al inicio de la lista '''
    def prepend(self, value):
        new_node = self.Node(value)
        '''Preguntamos si la lista esta vacía '''
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        #De lo contrario si la lista no esta vacía
        else:
            ''' Enlazamos el nuevo nodo con la actual cabeza de la lista '''
            new_node.next_node = self.head
            ''' Enlazamos la cola con la cabeza '''
            self.tail.next_node = new_node
            ''' Actualizamos la nueva cabeza de la lista '''
            self.head = new_node
        self.length += 1

    ''' Método para añadir nodos al final de la lista '''
    def append(self, value):
        new_node = self.Node(value)
        '''Preguntamos si la lista esta vacía '''
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        #De lo contrario si la lista no esta vacía
        else:
            self.tail.next_node = new_node
            new_node.next_node = self.head
            self.tail = new_node
        self.length += 1

    '''Creamos la función encargada de eliminar el primer nodo de la lista  '''
    def shift(self):
        if self.length ==0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.head
            ''' Actualizamos la cabeza de la lista '''
            self.head = remove_node.next_node
            ''' Enlazamos la cola con la nueva cabeza '''
            self.tail.next_node = self.head
            ''' Rompemos el enlace del nodo eliminado con la lista '''
            remove_node.next_node = None
            self.length -= 1
            print(remove_node.value)

    '''Creamos la función encargada de eliminar el ùltimo nodo de la lista  '''
    def pop(self):
        if self.length ==0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            new_tail = current_node
            cant_nodes_cll = self.length
            while cant_nodes_cll != 0:
                ''' El nodo siguiente es diferente de la cabeza '''
                if current_node.next_node != self.head:
                    new_tail = current_node
                    current_node = current_node.next_node
                else:
                    break
            self.tail = new_tail
            ''' El enlace siguiente de la cola apunta a la cabeza '''
            self.tail.next_node = self.head
            self.length -=1
            print(current_node.value)
            

class Tuple_list:
    def __init__(self):
        #Creamosuna lista:
        self.soccer_teams = []
        #Cantidad de equipos => tamaño de la lista
        self.list_length = 0
        #Variables que se contemplaran dentro de la tupla
        self.name_team = ""
        self.city_team = ""
        self.games_won = 0

    #Método para inicializar la lista
    def initialize_list(self):
        #Solicitar al usuario cantidad de equipos que conoce y validar que el input si sea un valor entero
        while True:
            try:
                self.list_length = int(input("Cantidad de equipos a ingresar\n          >>>"))
                print("             INFORMACIÓN DE EQUIPOS DE FUTBOL")
                for item in range(1, self.list_length + 1):
                    self.name_team = input("            > Equipo\n                  >>>")
                    self.city_team = input("            > Ciudad\n                  >>>")
                    while True:
                        try:
                            self.games_won = int(input("            > Cant. partidos\n                  >>>"))
                            break
                        except ValueError:
                            print("         >> Se esperaba un valor numérico <<")
                    #Add name and city of the soccer team as elements in the tuple that is content in a list
                    self.soccer_teams.append((self.name_team, self.city_team, self.games_won))
                print(self.soccer_teams)
                break
            except ValueError:
                print("         >> Se esperaba un valor numérico <<")

    #Eliminar un equipo por el nombre que indique el usuario. Se elimina la tupla: equipo y ciudad
    def delete_team(self):
        self.name_team = input("            Nombre del equipo a eliminar\n                  >>>")
        #Recorremos la lista de equipos
        for item_tuple in range(len(self.soccer_teams)):
            #Validar si el valor que hay en la primer posición de la tupla es igual al input del user
            if self.soccer_teams[item_tuple][0] == self.name_team:
                print("Se ha encontrado el equipo")
                #Eliminamos por la posicion que ocupa el equipo
                self.soccer_teams.pop(item_tuple)
                print(f"            >>> Lista de equipos actual: {self.soccer_teams} <<<")
                break
            
    def max_games_won_team(self):
        max_value = 0
        for item_tuple in range(1, len(self.soccer_teams)):
            if self.soccer_teams[item_tuple][2] > self.soccer_teams[max_value][2]:
                max_value = item_tuple
        print(f"El equipo que más partidos jugo en la temporada fue {self.soccer_teams[max_value][0]}")
            

            



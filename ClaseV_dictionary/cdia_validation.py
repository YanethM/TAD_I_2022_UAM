class CdiaValidation:
  def __init__(self):
    self.cdia_humasciiano = ""
    self.list = []
    self.adidas_dictionary = { #key : value
                                "Categorias": 4,
                                "Mujer": ["RopaM","TennisM","AccesoriosM","DeportesM"],
                                "Hombre": ["Ropa","Tennis","Accesorios","Deportes"]
    }

    self.adidas_dictionary2 = { 
                                "Mujer": [("REF123", 36, "Azul"),
                                          ("REF124", 37, "Blanco"),
                                          ("REF125", 38, "Negro")],
                                "Hombre": [("HREF123", 40, "Azul"),
                                          ("HREF124", 39, "Blanco"),
                                          ("HREF125", 41, "Negro")]
    }
  
  def keys_values(self):
    print(self.adidas_dictionary.keys())
    print(self.adidas_dictionary.values())
  
  def keys_mujer(self):
    #Diccionario inicia en la posición
    print(self.adidas_dictionary["Mujer"][1])
    print(self.adidas_dictionary2["Mujer"][1][0])
    #Tupla que se convertira en diccionario
    tuple_contact = dict({"name" : "Yaneth","age" : 31, "gender": "F"})
    print(tuple_contact.keys())


    for item in self.adidas_dictionary:
      print(self.adidas_dictionary[item])

  





  def validation(self):
    self.cdia_humasciiano = input("CDIA: >>>")
    print(self.cdia_humasciiano.upper())
    print(self.cdia_humasciiano.lower())
    if(len(self.cdia_humasciiano) == 3):
      self.list.append(self.cdia_humasciiano)
      print(self.cdia_humasciiano)


       

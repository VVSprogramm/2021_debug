#Klases nosaukumu

class Robots:
  """Klase reprezentā robotu ar specifisko vārdu"""
  
  #Klases konstruktoru. Inicializēšana.
  def __init__(self, vards):
    """Datu inicializācija"""

    #Īpašību definēšana
    self.vards=vards

    print(f"Incializējam {self.vards}")

  def sasveicinaties(self):
    print(f"Sveiks! Mani sauc {self.vards}")


#Klases pārbaudīšana

#1. robota izveide
rob1 = Robots("R1")

#1. robota metodes pārbaude
rob1.sasveicinaties()
rob1.sasveicinaties()

#2. robota izveide

rob2 = Robots("R2")

rob2.sasveicinaties()
  
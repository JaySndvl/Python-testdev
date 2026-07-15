class partyAnimal:
    
    def __init__(self):
        self.x = 0
        
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
        
an = partyAnimal()

an.party()
an.party()
an.party()
from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name

    def freebie(self):
        freebie_dev = []
        for i in Freebie.instances:
            if i.dev == self.name:
                pass

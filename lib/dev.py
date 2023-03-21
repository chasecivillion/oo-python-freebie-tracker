from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name

    def freebie(self):
        freebie_dev = []
        for i in Freebie.instances:
            if i.dev == self:
               freebie_dev.append(i)
        return freebie_dev
    
    def companies(self):
        freebies_companies = []
        for i in Freebie.instances:
            if i.dev == self:
                freebies_companies.append(i.company)
        return freebies_companies


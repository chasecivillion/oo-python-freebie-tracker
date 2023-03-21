from .freebie import Freebie

class Company:

    def __init__ (self, name, founding_year):
        self.name = name
        self.founding_year = founding_year

    def freebies(self):
        return_list = []
        for i in Freebie.all():
            print(Freebie.instances[0])
            if i.company == self:
                return_list.append(i)
        return return_list
    
    def devs(self):
        return_list = []
        for i in Freebie.all():
            if i.company == self:
                if not i.dev.name in return_list:
                    return_list.append(i.dev)
        return return_list
    

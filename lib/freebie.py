
class Freebie:
    instances = []
    
    def __init__(self, dev, company, item_column, value_column):
        self.dev = dev
        self.company = company
        self.item_column = item_column
        self.value_column = value_column
        Freebie.instances.append(self)

    @classmethod
    def all(cls):
        return cls.instances

    def print_details(self):
        print(f'{self.dev.name} owns a {self.item_column} from {self.company.name}')

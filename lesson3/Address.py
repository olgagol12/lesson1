class Address:
    def __init__(self, index, town, street, home, apt):
        self.index = index
        self.town = town
        self.street = street
        self.home = home
        self.apt = apt

    def __str__(self):
        return f"{self.index}, {self.town}, {self.street}, {self.home} - {self.apt}"

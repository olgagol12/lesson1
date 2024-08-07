class Smartphone:
    def __init__ (self, marka, model, nomer ):
        self.marka = marka
        self.model = model
        self.nomer = nomer

    def phone (self):
        print ( self.marka, "-", self.model, ".", self.nomer)

    def addcatalog (self, catalog):
        self.catalog = catalog



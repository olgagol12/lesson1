class User:
    def __init__ (self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name

    def sayfistname (self):
        print("имя",  self.first_name)

    def saylastname (self):
        print ("фалимия",  self.last_name)

    def lastfirst (self):
        print ("имя и фамилия",  self.first_name,  self.last_name )

alla = User ("alla", "don")
alla.sayfistname()
alla.saylastname()
alla.lastfirst()

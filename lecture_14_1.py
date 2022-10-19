# Sample class

# Define class
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


# Construct object
an = PartyAnimal()

# Call class method
an.party()
an.party()
an.party()

# See object type and available methods
print("Type:", type(an))
print("Capabilities:", dir(an))

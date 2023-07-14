##
## animals.py -- example of creating superclasses and subclasses with
##    inheritance. Describes household pets.
##
## 2023.07.13 - liac@umich.edu
## Created for WoCCode Summer Bootcamp
##--------------------------------------------------------------------

class HouseholdPet(object):
    """
    Household pet class

    Attributes
    ----------
    
    species : string, describes the animal species
    
    name : string, name of the pet
    
    color : string, describes the pet's color
    """
    def __init__(self, species, name, color):
        self.species = species
        self.name = name
        self.color = color
        
    def info(self):
        """
        Print the name, color, and species of the household pet
        """
        print("{} is a {} {}".format(self.name, self.color, self.species))

class DomesticCat(HouseholdPet):
    """
    Describes a domestic cat, a type of HouseholdPet

    Attributes
    ----------

    species : 'Felis Catus'
    
    name : string, name of the cat
    
    color : string, describes the cat's color
    """
    def __init__(self, name, color):
        HouseholdPet.__init__(self, 'Felis Catus', name, color)
    def speak(self):
        """
        Tells the cat to speak
        """
        print("meow")

class DomesticDog(HouseholdPet):
    """
    Describes a domestic cat, a type of HouseholdPet

    Attributes
    ----------

    species : 'Canus lupus familiaris'
    
    name : string, name of the dog
    
    color : string, describes the dogs's color
    """
    def __init__(self, name, color):
        HouseholdPet.__init__(self, 'Canis lupus familiaris', name, color)
    def speak(self):
        """
        Tells the dog to speak
        """
        print("woof")

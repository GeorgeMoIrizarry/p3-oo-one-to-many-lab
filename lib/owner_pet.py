# import ipdb 
class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    def __init__(self, name, pet_type, owner="Person"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_type):
        if not pet_type in self.PET_TYPES:
            raise TypeError('Pet type must be of on in approved list')
        self._pet_type = pet_type
class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, new_pet):
        if not isinstance(new_pet, Pet):
            raise TypeError('New pet must be of Pet class, a pet instance')
        new_pet.owner = self
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
# ipdb.set_trace()
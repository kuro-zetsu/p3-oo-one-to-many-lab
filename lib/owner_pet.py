class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError('pet must be of type Pet.')
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)
    
class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, p_type):
        if p_type not in Pet.PET_TYPES:
            raise ValueError('The pet must be in the list of approved pets.')
        self._pet_type = p_type
        
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if new_owner is not None and not isinstance(new_owner, Owner):
            raise TypeError('owner must be of type Owner or None.')
        self._owner = new_owner

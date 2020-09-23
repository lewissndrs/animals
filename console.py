import pdb
from models.owner import Owner
from models.animal import Animal
import repositories.owner_repository as owner_repository 
import repositories.animal_repository as animal_repository

owner_1 = Owner("Lewis")
owner_repository.save(owner_1)

owner_2 = Owner("Cyril")
owner_repository.save(owner_2)

animal_1 = Animal("Oscar", "Dog", owner_2)
animal_repository.save(animal_1)

animal_2 = Animal("Scooby Doo", "Dog", owner_2)
animal_repository.save(animal_2)

# animal_repository.delete(animal_2.id)

animal_repository.select_all()



pdb.set_trace()
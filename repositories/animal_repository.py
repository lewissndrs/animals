from db.run_sql import run_sql

from models.owner import Owner
from models.animal import Animal

import repositories.owner_repository as owner_repository


def save(animal):
    sql = 'INSERT INTO animals (name, species, owner_id) VALUES (%s, %s, %s) RETURNING *'
    values = [animal.name, animal.species, animal.owner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def delete(id):
    sql = 'DELETE FROM animals WHERE id = %s'
    values = [id]
    run_sql(sql,values)


def select_all():
    animals = []
    sql = 'SELECT * FROM animals'
    results = run_sql(sql)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['name'],row['species'],owner,row['id'])
        animals.append(animal)
    return animals
        
def select(id):
    animal = None
    sql = 'SELECT * FROM animals WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        animal = Animal(result['name'],result['species'],owner, result['id'])
    return animal

    def update(animal):
        sql = 'UPDATE animals SET (name, species, owner_id) = (%s,%s,%s) WHERE id = %s'
        values = [animal.name, animal.species, animal.owner_id, animal.id]
        run_sql(sql,values)
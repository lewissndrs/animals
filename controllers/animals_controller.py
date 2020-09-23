from flask import Flask, render_template, redirect, request 

from flask import Blueprint
from repositories import owner_repository, animal_repository
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/animals')
def view_list():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', all_animals=animals)

@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete(id):
    animal_repository.delete(id)
    return redirect ('/animals')

@animals_blueprint.route('/animals/new')
def new_animal():
    all_owners = owner_repository.select_all()
    return render_template("animals/new.html", all_owners=all_owners)

@animals_blueprint.route('/animals/new', methods=['POST'])
def create_animal():
    name = request.form['name']
    species = request.form['species']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    new_animal = Animal(name, species, owner)
    animal_repository.save(new_animal)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/show")
def get_animal(id):
    animal = animal_repository.select(id)
    return render_template("/animals/show.html", animal=animal)

@animals_blueprint.route('/animals/<id>/edit')
def edit_animal(id):
    animal = animal_repository.select(id)
    owners = owner_repository.select_all()
    return render_template("/animals/edit.html",all_owners = owners,animal=animal)

@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update_animal(id):
    name = request.form['name']
    species = request.form['species']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    animal = Animal(name,species,owner,id)
    animal_repository.update(animal)
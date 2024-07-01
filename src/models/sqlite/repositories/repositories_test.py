import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.people_repository import PeopleRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_list_pets():
    """
    Testando o método list_pets da classe PetsRepository.
    """
    pets_repository = PetsRepository(db_connection_handler)
    pets = pets_repository.list_pets()

    print(pets)

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_delete_pet():
    """
    Testando o método delete_pet da classe PetsRepository.
    """
    name = "belinha"

    pets_repository = PetsRepository(db_connection_handler)
    pets_repository.delete_pets(name)

    pets = pets_repository.list_pets()

    print(pets)

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_insert_person():
    first_name = "test Sandro"
    last_name = "test Sandro"
    age = 30
    pet_id = 1

    people_repository = PeopleRepository(db_connection_handler)
    people_repository.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_get_person():
    person_id = 1

    people_repository = PeopleRepository(db_connection_handler)
    response = people_repository.get_person(person_id = person_id)

    print("\n",response)
    print("\n",response.pet_name)

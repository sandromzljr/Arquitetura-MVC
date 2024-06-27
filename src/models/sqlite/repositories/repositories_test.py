
import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_list_pets():
    """
    Testando o método list_pets da classe PetsRepository.
    """
    pets_repository = PetsRepository(db_connection_handler)
    pets = pets_repository.list_pets()

    print(pets)

def test_delete_pet():
    """
    Testando o método delete_pet da classe PetsRepository.
    """
    name = "belinha"

    pets_repository = PetsRepository(db_connection_handler)
    pets_repository.delete_pets(name)

    pets = pets_repository.list_pets()

    print(pets)

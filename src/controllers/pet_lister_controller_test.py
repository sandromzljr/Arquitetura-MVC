from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name = "Thunder", type = "Dog", id = 1),
            PetsTable(name = "Garfield", type = "Cat", id = 2)
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "Thunder", "id": 1 },
                { "name": "Garfield", "id": 2 }
            ]
        }
    }

    assert response == expected_response

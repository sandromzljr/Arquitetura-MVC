from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.repositories.pets_repository import PetsRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                     PetsTable(name="Dog", type="Dog"),
                     PetsTable(name="Cat", type="Cat")
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, ex_tb):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)

    pets = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert pets[0].name == "Dog"

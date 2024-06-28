from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
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

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

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

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    pets_repository = PetsRepository(mock_connection)

    pets = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert pets == []

def test_delete_pets():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)

    pets_repository.delete_pets("petName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
    mock_connection.session.delete.assert_called_once()

def test_delete_pets_no_result():
    mock_connection = MockConnectionNoResult()
    pets_repository = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        pets_repository.delete_pets("petName")

    mock_connection.session.rollback.assert_called_once()

import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

@pytest.mark.skip(reason="Interação com o banco de dados SQLite.")
def test_connection():
    """
    Teste de integração com o banco de dados SQLite (storage.db).
    """
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)

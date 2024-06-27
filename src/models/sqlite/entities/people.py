from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)


    def __repr__(self):
        return f"<People(nome={self.first_name}, sobrenome={self.last_name}, idade={self.age}, pet_id={self.pet_id})>"

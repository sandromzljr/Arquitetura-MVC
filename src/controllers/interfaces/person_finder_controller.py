from typing import Dict
from abc import ABC, abstractmethod

class PersonFinderControllerInterface(ABC):

    @abstractmethod
    def find_person(self, person_id: int) -> Dict:
        pass

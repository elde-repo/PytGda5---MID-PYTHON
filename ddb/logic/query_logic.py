from abc import ABC, abstractmethod
from typing import List

class QueryLogic(ABC):
    @abstractmethod
    def control(self, document_name: str, columns: List[str], values: List[str]):
        pass

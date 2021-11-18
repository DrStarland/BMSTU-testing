import abc
from ..models import *

# (smotri file DjangoRepository, tam ssilki)
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def method(self):
        pass


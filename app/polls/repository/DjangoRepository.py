from polls.repository.abstractRepository import AbstractRepository
from . import AbstractRepository
from ..models import *


# https://www.cosmicpython.com/book/images/apwp_0205.png

# https://www.cosmicpython.com/book/chapter_02_repository.html
# https://lyz-code.github.io/blue-book/architecture/repository_pattern/

class DjangoRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

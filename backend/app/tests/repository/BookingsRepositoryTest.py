import os
import sys
path = os.environ["FILE_PATH"]
sys.path.append(path)

from testtool import TestCase

class BookeRepositoryTest(TestCase):
    def __init__(self,):
        self.repository = None

    def setUp(self):
        self.repository: Session = Depends(get_test_db)

    def test_create_user_repository(self):
        user = User()
        self.repository.add(user)
        self.repository.commit()
        self.repository.refresh()




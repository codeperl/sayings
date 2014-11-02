from sayings.models.repositories.user_repository import UserRepository


class UserService(object):
    """ UserService is a service do all user related tasks
    """

    def __init__(self, request):
        self.request = request
        self.user_repository = UserRepository()

    def insert(self, user):
        """ Initialize user object from request object and then insert data
        """
        self.user_repository.add(user)

    def update(self, user):
        """ Refine user object from request object and then update data
        """
        self.user_repository.update(user)

    def find_first_by_email(self, email):
        users = self.user_repository.find_first_by_email('a')
        return users

    def find_one_by_id(self, id):
        user = self.user_repository.find_one_by_id(id)
        return user

    def remove(self, user):
        if self.user_repository.delete(user):
            return True
        else:
            return False

    def find_all(self):
        return self.user_repository.all()
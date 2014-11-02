from sayings.models.repositories.role_repository import RoleRepository


class RoleService(object):
    """ RoleService is a service do all role related tasks
    """

    def __init__(self, request):
        self.request = request
        self.role_repository = RoleRepository()

    def insert(self, role):
        """ Initialize role object from request object and then insert data
        """
        self.role_repository.add(role)

    def update(self, role):
        """ Refine role object from request object and then update data
        """
        self.role_repository.update(role)

    def find_first_by_name(self, name):
        roles = self.role_repository.find_first_by_name('a')
        return roles

    def find_one_by_id(self, id):
        role = self.role_repository.find_one_by_id(id)
        return role

    def remove(self, role):
        if self.role_repository.delete(role):
            return True
        else:
            return False

    def find_all(self):
        return self.role_repository.all()
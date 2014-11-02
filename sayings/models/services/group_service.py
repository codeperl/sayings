from sayings.models.repositories.group_repository import GroupRepository


class GroupService(object):
    """ GroupService is a service do all group related tasks
    """

    def __init__(self, request):
        self.request = request
        self.group_repository = GroupRepository()

    def insert(self, group):
        """ Initialize group object from request object and then insert data
        """
        self.group_repository.add(group)

    def update(self, group):
        """ Refine group object from request object and then update data
        """
        self.group_repository.update(group)

    def find_first_by_name(self, name):
        groups = self.group_repository.find_first_by_name('a')
        return groups

    def find_one_by_id(self, id):
        group = self.group_repository.find_one_by_id(id)
        return group

    def remove(self, group):
        if self.group_repository.delete(group):
            return True
        else:
            return False

    def find_all(self):
        return self.group_repository.all()
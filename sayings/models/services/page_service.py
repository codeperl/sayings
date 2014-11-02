from sayings.models.repositories.page_repository import PageRepository


class PageService(object):
    """ PageService is a service do all page related tasks
    """

    def __init__(self, request):
        self.request = request
        self.page_repository = PageRepository()

    def insert(self, page):
        """ Initialize page object from request object and then insert data
        """
        self.page_repository.add(page)

    def update(self, page):
        """ Refine page object from request object and then update data
        """
        self.page_repository.update(page)

    def find_first_by_name(self, name):
        groups = self.page_repository.find_first_by_name('a')
        return groups

    def find_one_by_id(self, id):
        group = self.page_repository.find_one_by_id(id)
        return group

    def remove(self, page):
        if self.page_repository.delete(page):
            return True
        else:
            return False

    def find_all(self):
        return self.page_repository.all()
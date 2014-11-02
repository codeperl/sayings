from sayings.models.repositories.service_repository import ServiceRepository


class ServiceService(object):
    """ ServiceService is a service do all service related tasks
    """

    def __init__(self, request):
        self.request = request
        self.service_repository = ServiceRepository()

    def insert(self, service):
        """ Initialize service object from request object and then insert data
        """
        self.service_repository.add(service)

    def update(self, service):
        """ Refine service object from request object and then update data
        """
        self.service_repository.update(service)

    def find_first_by_name(self, name):
        services = self.service_repository.find_first_by_name('a')
        return services

    def find_one_by_id(self, id):
        service = self.service_repository.find_one_by_id(id)
        return service

    def remove(self, service):
        if self.service_repository.delete(service):
            return True
        else:
            return False

    def find_all(self):
        return self.service_repository.all()
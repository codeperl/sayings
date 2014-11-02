from sayings.models.repositories.product_repository import ProductRepository


class ProductService(object):
    """ ProductService is a service do all product related tasks
    """

    def __init__(self, request):
        self.request = request
        self.product_repository = ProductRepository()

    def insert(self, product):
        """ Initialize product object from request object and then insert data
        """
        self.product_repository.add(product)

    def update(self, product):
        """ Refine product object from request object and then update data
        """
        self.product_repository.update(product)

    def find_first_by_name(self, name):
        products = self.product_repository.find_first_by_name('a')
        return products

    def find_one_by_id(self, id):
        product = self.product_repository.find_one_by_id(id)
        return product

    def remove(self, product):
        if self.product_repository.delete(product):
            return True
        else:
            return False

    def find_all(self):
        return self.product_repository.all()
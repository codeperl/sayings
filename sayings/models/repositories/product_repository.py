from ..entities.product import Product
from .base_repository import BaseRepository
from webhelpers.text import urlify
from datetime import datetime


class ProductRepository(BaseRepository):
    def __init__(self):
        super(ProductRepository, self).__init__()
        self.product = Product

    def find_first_by_name(self, name):
        first = self.db_session.query(self.product).filter(self.product.name == str(name)).first()
        return first

    def find_one_by_id(self, id):
        product = self.db_session.query(self.product).filter(self.product.id == id).first()
        return product

    def add(self, product):
        if product.name:
            product.alias = urlify(product.name)

        product.created_at = datetime.now()

        self.db_session.add(product)
        self.commit()

        return product

    def update(self, product):
        if product.name:
            product.alias = urlify(product.name)

        product.updated_at = datetime.now()

        self.commit()

        return product

    def delete(self, product):
        try:
            self.db_session.delete(product)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.product).all()
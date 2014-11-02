from ..entities.service import Service
from .base_repository import BaseRepository
from webhelpers.text import urlify
from datetime import datetime


class ServiceRepository(BaseRepository):
    def __init__(self):
        super(ServiceRepository, self).__init__()
        self.service = Service

    def find_first_by_name(self, name):
        first = self.db_session.query(self.service).filter(self.service.name == str(name)).first()
        return first

    def find_one_by_id(self, id):
        service = self.db_session.query(self.service).filter(self.service.id == id).first()
        return service

    def add(self, service):
        if service.name:
            service.alias = urlify(service.name)

        service.created_at = datetime.now()

        self.db_session.add(service)
        self.commit()

        return service

    def update(self, service):
        if service.name:
            service.alias = urlify(service.name)

        service.updated_at = datetime.now()

        self.commit()

        return service

    def delete(self, service):
        try:
            self.db_session.delete(service)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.service).all()
try:
    import sqlalchemy
except ImportError:
    sqlalchemy = None

if sqlalchemy:
    from sqlalchemy import *
    from sqlalchemy.orm import *

    metadata = MetaData()

    from sayings.models.entities.User import User
    from sayings.models.repositories.user_repository import UserRepository

    user = User()
    userRepository = UserRepository()
    userRepository.add(user)


def connect(dsn):
    metadata.bind = create_engine(dsn)


def setup_mappers():
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
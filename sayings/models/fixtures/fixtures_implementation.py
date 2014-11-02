from fixture import SQLAlchemyFixture
from sqlalchemy import *
from sqlalchemy.orm import *
from sayings.models.fixtures import fixtures


fixtures.metadata.bind = create_engine("mysql://root:root@127.0.0.1/sayings_development?charset=utf8&use_unicode=0")
fixtures.metadata.create_all()
dbfixture = SQLAlchemyFixture(engine=fixtures.metadata.bind, env=fixtures)
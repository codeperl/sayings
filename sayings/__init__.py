from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from models.db_session import DBSession
from models.base import Base
from configs.router import Router
from extensions.jinja.sub_request.sub_request import SubRequestExtension

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    settings = merge_settings(settings)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config = add_routes_and_get_updated_config(config)
    config = add_http_common_page_view(config)
    config.scan('sayings.views')
    return config.make_wsgi_app()

def merge_settings(settings):
    """
    adding some required settings with given settings and return.
    """
    settings['jinja2.extensions'] = [SubRequestExtension]
    return settings

def add_routes_and_get_updated_config(config):
    """This function is adding routes and returns the updated
    config.
    """
    router = Router(config)
    router.add_routes()
    config = router.get_config()
    return config

def add_http_common_page_view(config):
    return config
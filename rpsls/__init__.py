from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = UnencryptedCookieSessionFactoryConfig('aJ8*hgYrTa%snH&fjhfek^JHEuK$ND&6HASJb^%hGhaSy')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("rpsls:templates")
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('play', '/throw')
    config.add_route('reset', '/reset')
    config.scan()
    return config.make_wsgi_app()
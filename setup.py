import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    # 'pyramid_chameleon',
    # 'pyramid_mako',
    'pyramid_jinja2',
    # Form creation
    #'deform',
    'pyramid_mailer',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    # To manage shared sessions for authentication and acl
    'pyramid_redis_sessions',
    'SQLAlchemy',
    # For inserting some default data in tables. Not successfully working.
    'fixture',
    # For inserting some default data in tables. Not successfully working.
    'fixture[sqlalchemy]',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    # To create automatic documentation.
    'docutils',
    # For database migrations.
    'alembic',
    # colendar alchemy may be needed to work with deform and alchemy model integration
    #'ColanderAlchemy'
    #forms with wtforms-alchemy
    'wtforms',
    'webhelpers',
    'WTForms-Alchemy'
    ]

setup(name='sayings',
      version='0.0',
      description='sayings',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='sayings',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sayings:main
      [console_scripts]
      initialize_sayings_db = sayings.scripts.initializedb:main
      """,
      )

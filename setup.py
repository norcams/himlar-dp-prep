import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'funcsigs',
    'pyramid',
    'pyramid_mako',
#    'pyramid_debugtoolbar',
#    'authomatic',
    'python-keystoneclient==5.0.1',
    'waitress',
    'grampg',
    'pika',
    ]

setup(name='himlar_dp_prep',
      version='0.0',
      description='himlar_dp_prep',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Jon K Hellan',
      author_email='jon.kare.hellan@uninett.no',
      url='https://github.com/norcams/himlar-dp-prep',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      dependency_links = [
          'http://github.com/norcams/authomatic/tarball/nrec#egg=authomatic-nrec/1.3.0'
      ],
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="",
      entry_points="""\
      [paste.app_factory]
      main = himlar_dp_prep:main
      """,
      )

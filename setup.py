from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='mongrel2_wsgi',
      version=version,
      description="Mongrel2 handler to WSGI.",
      long_description="""\
Mongrel2 to WSGI adapter based on CherryPy's WSGI server.
""",
      classifiers=[],
      keywords='wsgi mongrel2 eventlet',
      author='Daniel Holth',
      author_email='dholth@fastmail.fm',
      url='http://bitbucket.org/dholth/mongrel2_wsgi',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "pyzmq",
          "eventlet",
          "PasteScript",
          "PasteDeploy",
      ],
      entry_points="""
      [paste.server_runner]
      main = mongrel2_wsgi.runner:server_runner
      """,
      )

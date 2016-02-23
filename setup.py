from setuptools import setup, find_packages

version = '0.3'

setup(name='pleiades.atom',
      version=version,
      description="Atom formatting of Pleiades entities",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='atom plone georss pleiades',
      author='Sean Gillies',
      author_email='sgillies@frii.com',
      url='http://atlantides.org/trac/pleiades/pleiades.atom',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pleiades'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pleiades.geographer',
          'zope.datetime',
          'zope.dublincore',
          ],
      tests_require=[
          'pleiades.workspace'
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

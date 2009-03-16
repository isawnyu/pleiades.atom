from setuptools import setup, find_packages

version = '0.2'

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
          'pleiades.workspace'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

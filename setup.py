from setuptools import setup, find_packages
import os

version = '2.2b1dev'

setup(name='silva.translations',
      version=version,
      description="Translation for Silva CMS",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva translations',
      author='Infrae',
      author_email='info@infrae.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['silva'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.i18nmessageid',
          'zope.i18n',
          ],
      )

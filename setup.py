from distutils.core import setup

from setuptools import find_packages


setup(
    name='django-basemix',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    requires=['django', 'pendulum'],
    url='https://github.com/artscoop/django-basemix',
    license='BSD 3-clause',
    author='artscoop',
    author_email='artscoop@users.noreply.github.com',
    description='A set of useful model mixins for repetitive tasks'
)

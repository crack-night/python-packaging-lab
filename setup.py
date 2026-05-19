
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

# Por cada cambio es necesario actualizar la version 
setup(
    name='cracknight',
    version='2.5.2',
    packages=find_packages(),
    install_requires=[],
    author='Crack Night',
    description='Biblioteca para consultar cursos de Hack4U',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://hack4u.io'
)

# result: https://pypi.org/project/cracknight-hack4u/0.1.0/
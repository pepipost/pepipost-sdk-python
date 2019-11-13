from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='pepipost',
    version='2.6.0',
    description='Official Python Library by Pepipost for sending email using Web API v2',
    long_description=long_description,
    author='Vikram Sahu - DX Team, Pepipost & APIMatic',
    author_email='dx@pepipost.com',
    url='https://pepipost.com/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20.0, <3.0',
        'jsonpickle>=1.2.0, <2.0',
        'cachecontrol>=0.12.5, <1.0',
        'python-dateutil>=2.6.1, <3.0'
    ]
)

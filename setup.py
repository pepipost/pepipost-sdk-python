from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='pepipost',
    version='2.5.0',
    description='Official Python Library by Pepipost for sending email using Web API v2',
    long_description=long_description,
    author='Vikram Sahu - DX Team, Pepipost & APIMatic',
    author_email='dx@pepipost.com',
    url='https://pepipost.com/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)

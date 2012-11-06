try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'KitchenSink',
    version = '0.1.0',
    description = 'A collection of modules',
    author = 'Charlie Sharpsteen',
    author_email = 'source@sharpsteen.net',
    license = 'MIT',
    packages = find_packages()
)

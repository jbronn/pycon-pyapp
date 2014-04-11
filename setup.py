from setuptools import setup, find_packages

setup(
    version=__import__('pyapp').__version__,
    name='pyapp',
    author='Justin Bronn',
    author_email='jbronn@gmail.com',
    description='Toy Python (Django) App for my PyCon presentation',
    url='https://github.com/jbronn/pycon-pyapp',
    packages=find_packages(),
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="hotel-reservation-system",
    version="0.1",
    author="Nikhil",
    packages=find_packages(),
    install_requires=requirements
)
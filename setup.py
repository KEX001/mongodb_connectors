from setuptools import setup, find_packages

setup(
    name="mongodb-connectors",
    version="1.0.0",
    description="MongoDB Connection URI Manager",
    packages=find_packages(),
    install_requires=['pymongo>=4.0'],
    python_requires=">=3.8",
    author="KEX",
    author_email="--",
    url="https://github.com/KEX001/mongodb-connectors",
)

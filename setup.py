from setuptools import setup, find_packages

setup(
    name="mongodb-uri-repo",  # This is the PyPI/distribution name
    version="1.0.0",
    description="MongoDB URI Repository",
    packages=['mongodb'],  # Explicitly specify your package name
    install_requires=[],
    python_requires=">=3.6",
)

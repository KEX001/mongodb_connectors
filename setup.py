from setuptools import setup, find_packages

setup(
    name="mongodb",
    version="1.0.0",
    description="A repository of MongoDB connection URIs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="KEX001",
    url="https://github.com/KEX001/mongodb",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

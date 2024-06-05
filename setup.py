from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='sunday',
    version='0.9',
    description='System Using Neural Development Apis Yield',
    license="Apache 2.0",
    long_description=long_description,
    author='Marco Egea',
    author_email='markoegea@gmail.com',
    url="https://markoegea.onrender.com/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache 2.0 Software License',
        "Operating System :: OS Independent",
    ]
)
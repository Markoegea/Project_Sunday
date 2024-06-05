import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='sunday',
    version='0.9',
    description='System Using Neural Development Apis Yield',
    license="Apache 2.0",
    long_description=long_description,
    author='Marco Egea',
    author_email='markoegea@gmail.com',
    url="https://markoegea.onrender.com/",
    packages=setuptools.find_packages()
)
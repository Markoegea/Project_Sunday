from setuptools import setup

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
   packages=['sunday'],  #same as name
   install_requires=['joblib', 'numpy', 'scikit-learn', 'scipy', 'threadpoolctl'], #external packages as dependencies
   scripts=[
            'test',
            'main',
    ]
)

if __name__ == '__main__':
    print(long_description)
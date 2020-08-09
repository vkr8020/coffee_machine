from setuptools import setup, find_packages


packages = find_packages(
     include=['coffee_machine','coffee_machine.*'],
     exclude=['*.__pycache__.*']
    )


setup(name='coffee_machine',
      version='0.1.0',
      packages=packages,
      )

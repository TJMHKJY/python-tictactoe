from setuptools import setup

setup(name='python_tictactoe',
      version='0.1.0',
      packages=['python_tictactoe'],
      entry_points={
          'console_scripts': [
              'python_tictactoe = python_tictactoe.__main__:main'
          ]
      },
      )
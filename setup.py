from setuptools import setup

setup(name='NUMPY CRUNCHER DATA SCIENCE TEST',
      version='0.1',
      description='Creates and sums over large arrays to stress CPU with matrix operations',
      url='',
      author='peaceblaster',
      license='MIT',
      install_requires=[
          'numpy',
          'tqdm'
      ],
      zip_safe=False)
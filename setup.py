import io

from setuptools import setup, find_packages

def readme():
  with open('README.md') as f:
    return f.read()


setup(name='pymsf',
      version='0.0.1',
      description='Python script to conver msf to tsv',
      url='http://github.com/ypriverol/pymsf',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author='Yasset Perez-Riverol',
      author_email='ypriverol@gmail.com',
      license='LICENSE',
      include_package_data=True,
      install_requires=[
      ],
      scripts=['msf/pymsf.py'],
      packages=find_packages(),
      entry_points={
        'console_scripts': [
          'pymsf = msf.pymsf:main'
        ]},
      zip_safe=False)

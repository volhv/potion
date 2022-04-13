import subprocess

from setuptools import setup
from setuptools.command.install import install

try:
    cmd = ["pip", "install", '-r', 'requirements.txt']
    subprocess.run(" ".join(cmd), shell=True, check=True)
except:
    pass


VERSION = "22.3.1.1"

setup(name='potion',
      version=VERSION,
      cmdclass={
        'install': install,
      },
      zip_safe=False,
      description='Potion: data sources helper library',
      package_dir={'potion': 'src/potion'},
      packages=['potion'],
      entry_points={
        'console_scripts': []
      })

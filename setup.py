from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in order_packing/__init__.py
from order_packing import __version__ as version

setup(
	name="order_packing",
	version=version,
	description="This module is to ease kitchen packing management",
	author="Mubeen Ali",
	author_email="cmubeenali@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rtcpro/__init__.py
from rtcpro import __version__ as version

setup(
	name="rtcpro",
	version=version,
	description="custom style for rtcpro website",
	author="osama",
	author_email="osama@aoai.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

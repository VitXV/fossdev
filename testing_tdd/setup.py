from setuptools import (setup, find_packages)

setup(
	name = "ndfl_myatnik",
	version = "0.0.0",
	package_dir = {"": "src"},
	packages = find_packages(where="src"),
	long_description = "Tax calculator",
	long_description_content_type = "text/markdown"
)

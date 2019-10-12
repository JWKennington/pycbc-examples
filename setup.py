"""Setup file
"""

import setuptools

import pycbc_examples

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pycbc_examples',
                 version=pycbc_examples.__version__,
                 description='PyCBC Examples',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url=pycbc_examples.__github_url__,
                 author='James W. Kennington',
                 author_email='jameswkennington@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 zip_safe=False)

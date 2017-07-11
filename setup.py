from setuptools import setup, find_packages

with open('README.txt') as file:
    long_description = file.read()

setup(
    # MANDATORY fields
    # Metadata for upload to kick-pypi
    packages = find_packages(), # do not remove this line. used for adding files into package
    name = "mitodasghrepo", # same as template name
    author = "mitoda",
    author_email = "mitoda@cisco.com", # if author is supplied author_email is mandatory too
    url = "http://my-home-page.example.com",

    # OPTIONAL fields (see https://docs.python.org/2/distutils/setupscript.html for more)
    long_description = long_description,
    version = "5.0.0" # if not supplied default will be 0.0.0
    # description = "This is an Example Package"
    # install_requires = ['docutils>=0.3'] # for setting package dependencies
    # license = "Licensed to Dummy"
    # keywords = "hello world example examples"
)

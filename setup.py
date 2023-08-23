import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3', # Must match package folder name
    author='Curtis Erhart',
    author_email='curtis@kavaken.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CurtisAtKavaken/test_package',
    project_urls = {},
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
import setuptools


with open("README.md", "r") as file:
    long_description = file.read()


setuptools.setup(
    name='dnaclient',
    version='0.0.1',
    author='Codete',
    author_email='mail@codete.com',
    description='Dow Jones API client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/codete/dnaclient',
    packages=['dnaclient'],
    install_requires=[
        'markdown',
        'requests',
        'avro-python3'
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

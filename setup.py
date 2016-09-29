from setuptools import setup, find_packages

setup(
    name='pylcmodel',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/openmrslab/pylcmodel.git',
    license='MIT',
    author='bennyrowland',
    author_email='bennyrowland@mac.com',
    description='Local CLI to forward lcmodel commands to remote machine',
    install_requires=['parsley']
)

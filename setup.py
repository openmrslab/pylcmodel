from setuptools import setup, find_packages

with open("./pylcmodel/_version.py") as f:
    exec(f.read())

setup(
    name='pylcmodel',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/openmrslab/pylcmodel.git',
    license='MIT',
    author='bennyrowland',
    author_email='bennyrowland@mac.com',
    description='Local CLI to forward lcmodel commands to remote machine',
    install_requires=['parsley', 'cryptography', 'paramiko'],
    test_requires=['pytest']
)

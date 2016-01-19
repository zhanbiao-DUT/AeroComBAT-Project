from distutils.core import setup
import AeroComBAT

setup(
    name='AeroComBAT',
    description=AeroComBAT.__doc__,
    author='Ben Names',
    author_email='bennames@vt.edu',
    py_modules=['AeroComBAT'],
    version='0.2.1',
    license='MIT',
    install_requires=[
        'numpy',
        'mayavi']
    )
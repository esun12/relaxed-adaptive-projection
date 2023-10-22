from setuptools import setup

setup(
    name='rap',
    version='0.1.0',
    description='Relaxed Adaptive Projection (RAP) algorithm for private synthetic data generation.',
    author='Bard',
    author_email='elvissun811@gmail.com',
    url='https://github.com/',
    packages=['rap'],
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
    ],
)
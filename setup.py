from setuptools import setup

packages = ['relaxed_adaptive_projection']

package_data = {
    '': ['*'],
}

install_requires = ['numpy', 'scipy', 'scikit-learn']

setup_kwargs = {
    'name': 'rap',
    'version': '0.1.0',
    'description': 'Relaxed Adaptive Projection (RAP) algorithm for private synthetic data generation.',
    'author': 'Bard',
    'author_email': 'bard@google.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/esun12/relaxed-adaptive-projection',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<=3.9.12',
}


setup(**setup_kwargs)
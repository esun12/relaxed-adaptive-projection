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
    'long_description': '[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue)](https://www.python.org/)\n\n## Relaxed Adaptive Projection (RAP) algorithm\n\nThe RAP algorithm generates synthetic data that is consistent with a given distribution while preserving differential privacy.\n\n## Installation\n\n`\npip install rap\n`\n\n## Usage\n\nTo use the RAP algorithm, you can import the `rap` package and instantiate a `RAP` object. You can then call the `fit()` method to fit the model to your dataset and the `sample()` method to generate synthetic data.\n\nHere is an example of how to use the RAP algorithm to generate synthetic data:\n\n`python\nimport rap\n\n# Create a RAP object.\nrap = rap.RAP()\n\n# Fit the RAP model to the dataset.\nrap.fit(dataset)\n\n# Generate synthetic data.\nsynthetic_data = rap.sample(length=1000)\n`",
    'author': 'Bard',
    'author_email': 'bard@google.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/esun12/relaxed-adaptive-projection',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<=3.9',
}


setup(**setup_kwargs)
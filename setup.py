from setuptools import setup, find_packages
import os

requires = [
    'elasticsearch==2.4.0',
    'PyJWT==2.4.0',
    'iso8601==1.0.2',
    'six==1.16.0',
    'itsdangerous==1.1.0',
    'markupsafe==1.1.1',
    'flask-cors==3.0.10',
    'werkzeug==0.16.1',
]

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name = 'annotator',
    version = '0.14.2',
    packages = find_packages(exclude=['test*']),

    install_requires = requires,
    extras_require = {
        'docs': ['Sphinx'],
        'testing': ['Flask==1.1.4', 'mock', 'nose', 'coverage'],
        'flask': ['Flask==1.1.4'],
    },

    # metadata for upload to PyPI
    author = 'Rufus Pollock and Nick Stenning (Open Knowledge Foundation)',
    author_email = 'annotator@okfn.org',
    description = 'Database backend for Annotator (http://annotatorjs.org)',
    long_description = (read('README.rst') + '\n\n' +
                        read('CHANGES.rst')),
    license = 'MIT',
    keywords = 'annotation web javascript',

    url = 'http://annotatorjs.org/',
    download_url = 'https://github.com/openannotation/annotator-store',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
)

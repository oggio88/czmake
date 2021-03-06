from os.path import join, dirname
from setuptools import setup, find_packages


def read(fname):
    return open(join(dirname(__file__), fname)).read()


config = {
    'name': "czmake",
    'version': "0.5",
    'author': "Walter Oggioni",
    'author_email': "oggioni.walter@gmail.com",
    'description': ("Comelz build utility module."),
    'long_description': read('README.rst'),
    'license': "MIT",
    'keywords': "cmake",
    'url': "https://github.com/comelz/czmake",
    'packages': ['czmake', 'czmake/cmake', 'czmake/cmake/private'],
    'include_package_data': True,
    'package_data': {
        '': ['*.cmake'],
    },
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    "entry_points": {
        'console_scripts': [
            'czmake=czmake.czmake:run',
            'czmake-build=czmake.build:run',
            'czmake-configure=czmake.configure:run',
            'czmake-co=czmake.checkout:clone',
            'czmake-checkout=czmake.checkout:clone',
            'czmake-update=czmake.checkout:update',
            'czmake-up=czmake.checkout:update',
        ],
    }
}
setup(**config)

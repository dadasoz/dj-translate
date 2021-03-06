import os
import re
import uuid

from distutils.core import setup
from setuptools import find_packages
from pip.req import parse_requirements


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requirements = parse_requirements(
    os.path.join(PROJECT_ROOT, 'requirements.txt'), session=uuid.uuid1())

# e.g. ['django', 'google-api-python-client']
requirements = [str(ir.req) for ir in install_requirements]


setup(
    name='dj-translate',
    version='1.0.4',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    include_package_data=True,
    package_data={
        'autotranslate': ['templates/autotranslate/*.html',
                          'templates/autotranslate/css/*.css',
                          'templates/autotranslate/js/*.js',
                          'static/admin/img/*.png'
                          ],
    },
    zip_safe=False,
    license='MIT License',
    description='A simple Django app to automatically translate the pot (`.po`) files generated by django\'s '
                'makemessages command using google translate.',
    long_description=README,
    url='https://github.com/dadasoz/dj-translate/',
    author='Dadaso Zanzane',
    author_email='dada.z888@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

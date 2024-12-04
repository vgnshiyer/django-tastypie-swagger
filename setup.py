#!/usr/bin/env python

from setuptools import setup
import tastypie_swagger3

description = "An adapter to use swagger-ui with django-tastypie (compatible with Django >= 5.0)"

try:
    longdesc = open('README.rst').read()
except Exception:
    longdesc = description

setup(
    # Metadata
    name='django-tastypie-swagger3',
    version='.'.join(map(str, tastypie_swagger3.VERSION)),
    description=description,
    long_description=longdesc,
    author='Vignesh Iyer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Web Environment',
        'Framework :: Django 5.0',
    ],
    url='https://github.com/vgnshiyer/django-tastypie-swagger3',
    download_url='https://github.com/vgnshiyer/django-tastypie-swagger3/releases',
    license='BSD',
    packages=['tastypie_swagger3'],
    include_package_data=True,
    zip_safe=False,
)

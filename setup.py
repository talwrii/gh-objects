import setuptools
import distutils.core


setuptools.setup(
    name='gh-objects',
    version="1.0.0",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='Email',
    description='',
    license='GPLv3',
    keywords='github,gh,JSON,objects',
    url='',
    packages=["gh_objects"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['gh-objects=gh_objects.main:main']
    },
    test_suite='nose.collector'
)

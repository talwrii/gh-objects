import setuptools
import distutils.core


setuptools.setup(
    name='gh-things',
    version="1.1.1",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='Companion app for the Github CLI gh to fetch machine readable information about Github objects',
    license='GPLv3',
    keywords='github,gh,JSON,objects',
    url='https://github.com/talwrii/gh-things',
    packages=["gh_objects"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['gh-things=gh_things.main:main']
    }
)

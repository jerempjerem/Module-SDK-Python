from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pip>=21.1', 'termcolor>=1.1.0', 'httpx>=0.20.0']

test_requirements = ['pytest>=3', ]

setup(
    author="jerempjerem",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        
    ],
    description="A python SDK for The Module API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['opensea', 'nft', 'non fungible token', 'crypto', 'stream'],
    maintainer='Jerem',
    name='module_sdk',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    test_suite='tests',
    url='https://github.com/jerempjerem/Module-SDK-Python',
    project_urls={
        'Source': 'https://github.com/jerempjerem/Module-SDK-Python'
    },
    version='0.1.1',
    zip_safe=False,
)
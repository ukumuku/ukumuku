from setuptools import setup, find_packages

setup(
    name='ukumuku',
    version='0.0.1',
    url='https://github.com/ukumuku/ukumuku',
    install_requires=[
        'falcon==1.4.1',
        'Mako==1.0.7',
        'python-binary-memcached==0.26.1'
    ],
    description="ukumuku",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ]
)
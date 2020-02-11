from setuptools import setup, find_packages

setup(name='notie',
    version='1.0',
    url='https://github.com/sonowz/server-notie',
    author='sonowz',
    author_email='dnsdhrj123@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={"console_scripts": [
        "notie-welcome=notie.welcome:main",
        "notie-command=notie.commands:cli",
        "notie-schedule=notie.schedule:main"
    ]},
    zip_safe=False)
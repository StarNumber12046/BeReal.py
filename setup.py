from setuptools import setup, find_packages

setup(
    name='BeReal',
    version='1.0.0',
    description='BeReal API wrapper for Python (unofficial)',
    author='StarNumber',
    author_email='your@email.com',
    url='https://github.com/your-username/your-package',
    packages=find_packages(include=["BeReal"]),
    install_requires=[
        "requests"
    ],
)
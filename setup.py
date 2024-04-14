from setuptools import setup, find_packages

setup(
    name='leitner',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'leitner = leitner.__main__:main'
        ]
    },
    install_requires=[
    ],
)

from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='1.0',
    packages=find_packages(),
    install_requires=[     
        'flask',
        'python-dotenv',
        'json', 
        'pickle',
        'numpy',
        'flask_cors',
        'os'
    ],
)
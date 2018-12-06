import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'pydfcrypto',
    version = '0.1.0',
    author = ['Ryan Price'],
    author_email = ['ryapric@gmail.com'],
    description = 'Utilities to fully encrypt contents of whatever can fit in a Pandas DataFrame',
    long_description = long_description,
    url = 'https://www.github.com/ryapric/dfcrypto',
    packages = setuptools.find_packages(),
    python_requires = '>=3.6.*',
    install_requires = [
        'cryptography>=2.4.0',
        'pandas>=0.23.4'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points = {
        'console_scripts': [
            'pydfcrypto-encrypt=pydfcrypto.fileops.encrypt_main:main',
            'pydfcrypto-decrypt=pydfcrypto.fileops.decrypt_main:main'
        ]
    },
    include_package_data = True
)

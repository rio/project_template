from setuptools import setup, find_packages

setup(
    name="myapp",
    version="0.1.0",

    install_requires=["jsonrpc_utils==0.1.0", ],

    packages=find_packages(),

    entry_points={"console_scripts": ["myapp=myapp:main", ]}
)

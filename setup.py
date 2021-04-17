import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vanty-installer",
    version="0.0.5",
    author="Themba Mahlangu",
    author_email="themba@advantch.com",
    description="Vanty Installer Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.advantch.com/",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'vanty = vanty_installer.__main__:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'cookiecutter>=1.7.2',
        'PyYAML>=5.3.1'
    ],
    python_requires='>=3.7'
)

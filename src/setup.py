import setuptools

with open("README.md") as fh:
    long_description = fh.read()

try:
    REQUIREMENTS = list(open("requirements.txt").read().splitlines())
except OSError:
    REQUIREMENTS = []

packages = setuptools.find_packages("src")

assert packages, "No packages found"

setuptools.setup(
    name="palindromepal",
    version="0.0.1",
    author="Salim Fadhley",
    author_email="salimfadhley@gmail.com",
    description="Palindrome Pal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=packages,
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=REQUIREMENTS,
)

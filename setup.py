"""schlag package setup.
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="schlag",
    version="0.0.1",
    author="Daniel Wessel",
    author_email="daniel.wessel@motius.de",
    description="Schlager lyrics generation using transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["schlag"],
    python_requires=">=3.8",
)


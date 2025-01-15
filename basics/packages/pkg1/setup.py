from setuptools import setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="pkg1",
    version="0.0.1",
    author="Sergio Maffra",
    author_email="sergio.maffra@riskcare.com",
    description="Simple example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={},
    classifiers=[],
    install_requires=["numpy", "pandas", "matplotlib"],
    python_requires=">=3.10"
)

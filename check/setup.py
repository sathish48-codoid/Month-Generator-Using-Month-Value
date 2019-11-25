import setuptools
# import gitubuntu.source_information

with open("/home/codoid-dev/PycharmProjects/Month-Generator-Using-Month-Value/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Month generator", # R eplace with your own username
    version="0.0.1",
    author="sathish",
    author_email="samsathish48@gmail.com",
    description="It generate month using current month value",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sathish48-codoid/Month-Generator-Using-Month-Value",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
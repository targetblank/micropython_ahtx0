import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython-ahtx0",
    version="0.1.1",
    author="Andreas Bühl",
    author_email="code@abuehl.de",
    description="MicroPython driver for the AHT10 and AHT20 temperature and humidity sensors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="aht10, aht20, micropython, temperature, humidity, sensor, i2c",
    url="https://github.com/targetblank/micropython_ahtx0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)

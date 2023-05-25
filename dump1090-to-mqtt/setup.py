from setuptools import setup, find_packages

setup(
    name='dump1090-to-mqtt',
    description='',
    packages=find_packages(exclude=("tests",)),
    version='0.0.1',
    install_requires=[
        "aiohttp==3.8.4",
        "asyncio-mqtt==0.16.1",
    ],
    entry_points={
        "console_scripts": ["dump1090-to-mqtt = dump1090_to_mqtt.cli:typer_app"]
    },
    python_requires='>=3.11.3'
)

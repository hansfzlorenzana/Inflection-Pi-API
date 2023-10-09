from setuptools import setup, find_packages
from pathlib import Path

base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text(encoding='utf-8')

VERSION = '0.1.2'
DESCRIPTION = 'A reverse engineered API for Inflection AI Personal Intelligence, called PI'
LONG_DESCRIPTION = 'A reverse engineered API for Inflection AI Personal Intelligence, called PI'

setup(
    name="inflection-pi-api",
    version=VERSION,
    author="Hans FZ Lorenzana",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=['httpx', 'websocket-client', 'requests_toolbelt', 'loguru'],
    extras_require={
        'proxy': ['ballyregan; python_version>="3.9"']
    },
    keywords=['python', 'pi-api', 'inflection', 'chatgpt', 'pi', 'ai', 'api', 'chatbot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/hansfzlorenzana/Inflection-Pi-API",
    project_urls={"Bug Report": "https://github.com/hansfzlorenzana/Inflection-Pi-API/issues/new"}
)
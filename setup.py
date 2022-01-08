
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import re
from pathlib import Path

# Get readme from README.md.
readme = ''
repo_home = Path(__file__).resolve().parents[0]
readme_path = repo_home / 'README.md'
if readme_path.is_file():
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

# Get version number from debian/changelog.
chlog_path = repo_home / 'debian' / 'changelog'
with open(chlog_path, 'r') as f:
    first_line = f.readline()
version = re.match('.*\((.*)\).*', first_line).group(1)


setup(
    long_description=readme,
    name='Wasta TrafficToll',
    version=version,
    description='NetLimiter-like bandwidth limiting and QoS for Linux',
    python_requires='==3.*,>=3.6.0',
    project_urls={"homepage": "https://github.com/wasta-linux/python3-traffictoll", "repository": "https://github.com/wasta-linux/python3-traffictoll"},
    author='Chris Braun, Nate Marti',
    author_email='nate_marti@sil.org',
    license='GPLv3',
    keywords='traffic traffic control traffic shaping tc netlimiter qos',
    entry_points={"console_scripts": ["tt = traffictoll.__main__:main"]},
    packages=['traffictoll'],
    package_dir={"": "."},
    package_data={},
    install_requires=['psutil==5.*,>=5.6.7', 'ruamel.yaml==0.*,>=0.16.6'],
    extras_require={"dev": ["black==19.*,>=19.10.0.b0", "mypy==0.*,>=0.761.0"]},
)

import os
import shutil

import setuptools


def setup():
    with open('requirements.txt') as text_file:
        requirements = text_file.read().splitlines()

    setuptools.setup(
        packages=setuptools.find_packages(),
        install_requires=requirements,
        python_requires='>=3.10.0',
        include_package_data=True,
        author='biantsh',
        version='0.0.1',
        name='en-predictant',
    )

    # Remove installation artifacts
    build_path = 'build/'
    if os.path.exists(build_path):
        shutil.rmtree(build_path)

    egg_info_path = 'en_predictant.egg-info'
    if os.path.exists(egg_info_path):
        shutil.rmtree(egg_info_path)


if __name__ == '__main__':
    setup()

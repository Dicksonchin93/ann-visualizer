from setuptools import setup
import os

with open("README.md") as readme_file:
    readme = readme_file.read()


def read_requirements(fname):
    with open(fname) as requirements_file:
        requirements = requirements_file.read().split("\n")
        return [x for x in requirements if x.strip() != ""]

# get __version__ from keras_architecture_visualizer version file
exec(open(os.path.join("keras_architecture_visualizer", "version.py")))


requirements = read_requirements("requirements.txt")
test_requirements = requirements

setup_requirements = ["pytest-runner"]


setup(
    name='keras_architecture_visualizer',
    packages=['keras_architecture_visualizer'],
    version=__version__,
    license="MIT",
    description='A Python Library for visualizing Keras Neural Networks Models',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Chin Ee Kin',
    author_email='dickson_chin93@hotmail.com',
    url='https://github.com/Dicksonchin93/keras-architecture-visualizer',
    download_url='',
    keywords=['ann', 'ai', 'visualizer', 'learning', 'artificial', 'intelligence'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
)

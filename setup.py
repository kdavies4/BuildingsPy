import os
from setuptools import setup
# Python setup file. 
# See http://packages.python.org/an_example_pypi_project/setuptools.html

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "buildingspy",
    version = "1.4.0",
    author = "Michael Wetter",
    author_email = "mwetter@lbl.gov",
    description = ("Package for simulating and testing models from the Modelica Buildings and Annex 60 libraries"),
    long_description = read('buildingspy/README.rst'),
    license = "3-clause BSD",
    keywords = "modelica dymola openmodelica mat",
    url = "http://simulationresearch.lbl.gov/modelica/",
    install_requires = ['scipy', 'modelicares'],
    requires = ['scipy', 'modelicares (>=0.11.0)'],
    packages = ['buildingspy',
                'buildingspy/development', 
                'buildingspy/examples', 
                'buildingspy/io', 
                'buildingspy/simulate', 
                'buildingspy/thirdParty',
                'buildingspy/thirdParty.dymat',
                'buildingspy/thirdParty.dymat.DyMat',
                'buildingspy/thirdParty.dymat.DyMat.Export'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities"
    ],
)

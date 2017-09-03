from setuptools import setup, find_packages
setup(
    name="QtCompat",
    version="0.1",
    packages=find_packages(),
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[],

    package_data={
    },

    # metadata for upload to PyPI
    author="Jacob Schaer",
    author_email="",
    description="PyQt4, 5 and Pyside Compatibility Library",
    license="MIT",
    keywords="pyqt4 pyqt5 pyside compatibility",
    url="https://github.com/jacobschaer/qt_compat/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
import io
from setuptools import setup

with io.open('README.md') as f:
    long_description = f.read()

setup(
    name='axil-autotime',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Lev Maximov',
    description='An improved version of Time everything in IPython by Phillip Cloud',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache',
    url='https://github.com/cpcloud/ipython-autotime',
    use_scm_version={'write_to': 'autotime/_version.py'},
    setup_requires=['setuptools_scm'],
    install_requires=['ipython', 'monotonic ; python_version < "3.3"'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
    ],
    packages=['autotime'],
    zip_safe=False,
)

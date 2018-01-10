"""
chrome-cut
-------------

Basic command line tool to scan, detect, stream and control chrome cast
devices. \n
"""
from setuptools import setup


setup(
    name='Chrome-Cut',
    version='0.1',
    url='https://github.com/mrf345/chrome-cut-cli/',
    download_url='https://github.com/mrf345/chrome-cut-cli/archive/0.3.1.tar.gz',
    license='MPL 2.0',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='Command line tool to scan and control chrome cast devices.',
    long_description=__doc__,
    packages=['chrome_cut'],
    entry_points={
        'console_scripts': ['chrome-cut=chrome_cut.cli:cli']
    },
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests',
        'click',
        'netifaces'
    ],
    keywords=['chrome', 'cast', 'chromecast', 'control', 'monitor',
              'restore', 'stream', 'scan'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security', 'Topic :: System :: Monitoring',
        'Topic :: Utilities'
    ]
)

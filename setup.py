from setuptools import setup
from vncrecordingserver import __version__

setup(
    name='VncRecordingServer',
    version=__version__,
    long_description=__doc__,

    license='MIT',
    author='Patrick Jahns',
    author_email='github@patrickjahns.de',
    url='https://github.com/patrickjahns/vncrecordingserver',
    include_package_data=True,
    zip_safe=False,
    packages=[
        'vncrecordingserver'
    ],

    entry_points={
        'console_scripts': [
            'vncrecordingserver = vncrecordingserver:run',
        ],
    },
    install_requires=[
        'Flask==0.12.3',
        'vnc2flv==0.1.0'
    ],
    dependency_links=[
        'git+ssh://github.com/patrickjahns/vnc2flv.git@0.1.0#egg=vnc2flv-0.1.0',
    ]
)

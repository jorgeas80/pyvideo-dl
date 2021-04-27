from setuptools import setup

requirements = [
    'tldextract',
    'pytube',
    'twitter_dl @ git+https://github.com/jorgeas80/twitter-video-downloader.git@v0.1.0-alpha'
]

setup(
    name='pyvideo-dl',
    version='0.1.0',
    description='Library for Social Media video downloading',
    author='Jorge Arévalo',
    author_email='jorgeas80@tuta.io',
    license='MIT',
    url='https://github.com/jorgeas80/pyvideo-dl',
    keywords=['twitter', 'youtube', 'video', 'download'],
    install_requires=requirements,
    extras_require={
        'dev': [
            'ipython',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Conversion',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)

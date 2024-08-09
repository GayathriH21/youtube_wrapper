from setuptools import setup, find_packages 

setup(
    name='youtube_wrapper',
    version='0.1.0',
    description='A Python package to interact with YouTube Data API and YouTube Transcript API.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'youtube-transcript-api',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

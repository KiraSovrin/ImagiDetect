from setuptools import setup, find_packages

setup(
    name='ImagiDetect',        
    version='0.1',              
    packages=find_packages(),
    install_requires=[
        
        'PyQt5==5.15.4',
        
    ],
    entry_points={
        'console_scripts': [
            'imagidetect=imagidetect.main:main',  # Change 'main' to your actual entry point
        ],
    },
    author='Kira Sovrin',          
    author_email='',  
    description='',  
    
    long_description='',
    
    url='https://github.com/KiraSovrin/ImagiDetect.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        
    ],
)

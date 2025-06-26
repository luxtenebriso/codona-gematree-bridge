from setuptools import setup, find_packages

setup(
    name='codona_gematree_bridge',
    version='0.1.0',
    description='A symbolic integration bridge between GemaTreeAC gematria trees and Codona capsule outputs',
    author='Goldie & Jaakko',
    author_email='your_email@example.com',
    url='https://github.com/luxtenebriso/codona-gematree-bridge',
    packages=find_packages(),
    py_modules=['gematree_to_codona'],
    entry_points={
        'console_scripts': [
            'codona-capsule=gematree_to_codona:generate_codona_capsule'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    python_requires='>=3.7',
)

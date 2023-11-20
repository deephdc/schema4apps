from setuptools import setup

setup(
    name='ai4-metadata-validator',
    version='0.1.0',
    description='AI4OS Hub applications metadata validator',
    url='https://github.com/ai4os/ai4-metadata-validator',
    author='Álvaro López García',
    author_email='aloga@ifca.unican.es',
    license='Apache 2.0',
    packages=['ai4metav'],
    package_dir={'ai4metav': 'ai4metav'},
    package_data={'ai4metav': ['schemata/ai4-apps.json']},
    install_requires=[
        'jsonschema>=3.0.0b3',
        'rfc3987>=1.3.8',
        'simplejson>=3.16.0'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['ai4-metadata-validator=ai4metav.main:validate']
    }
)

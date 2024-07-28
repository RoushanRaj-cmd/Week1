from setuptools import find_packages, setup

package_name = 'week1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    py_modules=[
        'scripts.integer_generator',
        'scripts.odd_even_classifier',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='roushan',
    maintainer_email='roushan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'integer_generator = scripts.integer_generator:main',
            'odd_even_classifier = scripts.odd_even_classifier:main',
        ],
    },
)

from setuptools import setup

setup(name='introspectionparser',
      version='0.1',
      description='Parses introspection json output to OpenStack prettytable form',
      url='https://github.com/ervikrant06/Parse_json_introspection_data',
      author='Vikrant Aggarwal',
      author_email='vaggarwa@redhat.com',
      packages=['introspectionparser'],
      install_requires=[
          'prettytable'
      ],
      platforms=['Linux'],
      package_dir={'introspectionparser': 'introspectionparser'},
      entry_points={
          'console_scripts': [
              'introspectionparser=introspectionparser:main',
          ],
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Topic :: Text Editors :: Text Processing',
          'Topic :: Text Processing :: Markup :: XML',
      ],
)

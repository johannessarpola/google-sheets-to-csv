from setuptools import setup, Command
import os
def readme():
    with open('readme.md') as f:
        return f.read()

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(name='GSR',
      version='1.1',
      description='Google Sheets Retriever',
      url='https://tuki.pengon.fi',
      author='Johannes Sarpola',
      author_email='johannes.sarpola@pengon.fi',
      license='MIT',
	  packages=['GSR'],
      install_requires=[
          'google-api-python-client',
          'httplib2'
      ],
      long_description=readme(),
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False,
      cmdclass={
        'clean': CleanCommand,
    })

from setuptools import setup

def readme():
    with open('readme.md') as f:
        return f.read()

setup(name='GSR',
      version='1.01',
      description='Google Sheets Retriever',
      url='https://tuki.pengon.fi',
      author='Johannes Sarpola',
      author_email='johannes.sarpola@pengon.fi',
      license='MIT',
	  packages=['Utils'],
      install_requires=[
          'google-api-python-client',
          'httplib2'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)

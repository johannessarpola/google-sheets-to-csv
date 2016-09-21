from setuptools import setup

setup(name='GSR',
      version='1.0',
      description='Google Sheets Retriever',
      url='https://tuki.pengon.fi',
      author='Johannes Sarpola',
      author_email='johannes.sarpola@pengon.fi',
      license='MIT',
	  packages=['Lib'],
      install_requires=[
          'google-api-python-client',
          'httplib2'
      ],
      zip_safe=False)

from setuptools import setup, Command
import markdown2
import os
import codecs
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

class ConvertReadme(Command):
    """ Converts readme.md to readme.html """
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        head = '<!DOCTYPE html> <html lang="en"><head><meta charset="utf-8"><style type="text/css">'
        cssin = open("github.css")
        css = cssin.read()
        cssend = '</style></head><body>'
        print('start compile')
        fi = codecs.open('readme.md', 'r', 'utf-8')
        lines = fi.readlines()
        combinedList = ''.join(lines)
        mdlines = markdown2.markdown(combinedList, extras=["code-friendly", "fenced-code-blocks", "cuddled-lists", "footnotes", "numbering", "tables"])
        os.remove('readme.html')
        fo = codecs.open('readme.html', 'a', 'utf-8')
        fo.write(head)
        fo.write(css)
        fo.write(cssend)
        fo.write(str(mdlines))
        fi.close()
        fo.close()
        print('compile done')

setup(name='GSR',
      version='1.2',
      description='Google Sheets Retriever',
      url='https://tuki.pengon.fi',
      author='Johannes Sarpola',
      author_email='johannes.sarpola@pengon.fi',
      license='MIT',
	  packages=['GSR'],
      install_requires=[
          'google-api-python-client',
          'httplib2',
          'markdown2'
      ],
      long_description=readme(),
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False,
      cmdclass={
        'clean': CleanCommand,
        'compile': ConvertReadme
    })

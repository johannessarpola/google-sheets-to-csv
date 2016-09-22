from setuptools import setup, Command
import os
import codecs
import datetime

now = datetime.datetime.now()
authorName = 'Johannes Sarpola'
authorEmail = 'johannes.sarpola@pengon.fi'
supportUrl = 'https://tuki.pengon.fi'
currentYear = now.year
projectName = 'GSR'

def readme():
    with open('readme.md') as f:
        return f.read()

def createHeadWithCss(cssfilename):
    head = '<!DOCTYPE html> <html lang="en"><head><meta charset="utf-8"><style type="text/css">'
    cssin = open(cssfilename) # ("github.css")
    css = cssin.read()
    cssend = '</style></head><body>'
    return head+css+cssend

def createFooter():
    return ('<footer>'
        +'<div> <p>'+projectName+' | '
        +'Copyright (c)'+str(currentYear)+'  '+authorName+' | '
        +'Contact: '+authorEmail+'</p></div>'
        +'</footer>')

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
        import markdown2
        try:
            print('start compile')
            header = createHeadWithCss("github.css")
            fi = codecs.open('readme.md', 'r', 'utf-8')
            lines = fi.readlines()
            combinedList = ''.join(lines)
            mdlines = markdown2.markdown(combinedList, extras=["code-friendly", "fenced-code-blocks", "cuddled-lists", "footnotes", "numbering", "tables"])
            os.remove('readme.html')
            fo = codecs.open('readme.html', 'a', 'utf-8')
            fo.write(header)                # Add header with CSS stylesheets
            fo.write(str(mdlines))          # Add body
            fo.write('</body>')             # End body
            fo.write(createFooter())        # Add footer
            fi.close()
            fo.close()
            print('compile done')
        except ImportError:
            print('use py setup.py develop first')

setup(name=projectName,
      version='1.2',
      description='Google Sheets Retriever',
      url=r'https://tuki.pengon.fi',
      author=authorName,
      author_email=authorEmail,
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

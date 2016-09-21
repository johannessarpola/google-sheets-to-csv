from __future__ import print_function
import logging
import os
import codecs
import httplib2
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import SheetsManager
"""
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
"""
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
JSONSTORE = '.store'
OUTPUT_FOLDER = 'out'
CLIENT_SECRET_FILE = os.path.join(JSONSTORE, 'client_secret.json')
SHEET_CONF = os.path.join(JSONSTORE, 'sheet-ids.json')
APPLICATION_NAME = 'Sheet retriever'

logger = logging.getLogger('SheetRetriever')
def configureLogging():
    logging.basicConfig(filename='main.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gsheets.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def createSheetsService(http):

    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
    # Discover service
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    return service
def authenticateHttp(credentials):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    return http

def createSheetsManager(filename):
    manager = SheetsManager.Manager(filename)
    return manager

def doRetrievalCall(sheetService, sheetId, sheetRange):
    result = sheetService.spreadsheets().values().get(
        spreadsheetId=sheetId, range=sheetRange).execute()
    values = result.get('values', [])
    return values

def outputData(folder, filename, data):
    absFolder = os.path.abspath(folder)
    if not os.path.exists(absFolder):
        os.makedirs(folder)
    realp =os.path.join(folder,filename+'.csv')
    f = codecs.open(realp,'w', 'utf-8')
    f.writelines(str(data))
    f.close()

def transformDataToCsv(data):
    outStr = ''
    for row in data:
        outStr += '"'+'","'.join(row)
        outStr += '"'+os.linesep
    return outStr

def main():
    configureLogging()
    logging.info("Started retrieval")
    credentials = get_credentials()
    logging.info("Got credentials")
    # Authorize calls 
    http = authenticateHttp(credentials)
    logging.info("HTTP Authenticated")

    sheetsService = createSheetsService(http)
    logging.info("Created Google Sheets service")
    manager = createSheetsManager(SHEET_CONF)
    logging.info("Created SheetManager")

    while manager.hasNext():
        s = manager.getNext()
        sheetid = s.idstr
        wsheets = s.sheetslist
        sheetname = s.name # create output filename from sheet + wsheet
        for wsheet in wsheets:
            data = doRetrievalCall(sheetsService, sheetid, wsheet)
            wsheetoutName = sheetname+'_'+wsheet
            dataStr = transformDataToCsv(data)
            outputData(OUTPUT_FOLDER, wsheetoutName, dataStr)
            logging.info("Created CSV for "+wsheetoutName)

if __name__ == '__main__':
    main()
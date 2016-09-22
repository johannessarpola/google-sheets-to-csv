# What does it do

Retrieves the set sheets and their worksheets from Google Sheets and outputs CSVs with their
data.

Flow diagram

First run:
- Run SheetRunnable.py
- Give permission for the relevant Google account
- .credits/gsheets.json gets generated (token)

2.+ runs:
- Run SheetRunnable.py
- Gets sheets defined in sheet-ids.json and worksheets
- outputs to csv in ./out/ folder

Read to wherever you want the CSV afterwards.

# HOWTO

1. Install Python2.7, (included in distribution, not in git) (remember to tick the option to include in PATH if on Windows)
2. Run 'py setup.py develop' from commandline (if you have other python versions installed then it's 'py -2.7 setup.py develop'
3. Follow instructions on https://developers.google.com/sheets/quickstart/python on
how to create client_secret.json for a user
    - Notice that the downloaded file needs to be renamed to client_secret.json
4. configure sheet-ids.json to retrieve all the necessary sheets and sheets
    - "SpreadSheet1" : { ... defines the name for the sheet
    - "id":"1pNaDgWk6vrUxLwfA81nPUP06_fLqZCFmlUsrG1Z0RdI" ... defines the id for the sheet
    (instructions on how to get this are on the developers.google.com link above)
    - "Sheets": [ ... inside this worksheets are defined
5. Run GSR/SheetsRunnable.py and accept the permission (this nees to be done once)
	- command is 'py (-2.7) SheetRunnable.py'. The part in parenthesises is if there are multiple versions of Python installed, if only 2.7 ignore.
6. Run GSR/SheetsRunnable.py (or schedule) again
7. A folder called out is created and in it are CSV files for the configured sheets

# FAQ

- Python version?
> 2.7 as Goole API client wont work on 3.x, will probably change at some point.
Follow progress here https://github.com/google/google-api-python-client

- Safe?
> Yes, pretty much. If you modify the source code, it's on your own responsibility.

- Do I have to give permission for Google Sheets?
> Yes, how else would it allow to read files

- Will the permission expire at some point?
> Generally they do, but couldn't find specifics. Should be quite simple to regenerate the permission by just removing C:\\Users\\USERNAME\\.credentials\\gsheets.json and rerun.

- Does the application have access to change anything?
> No, it's readonly. Although you still need to take care with client_secret.json
as it's basically your login details but not in clear text format. You can always
revoke access through http://console.developers.google.com/

- I borked JSON structure and everthing fails?
> Redo from original development, take
care that all special characters are closed and commas where they should be.

- Logging?
> yes, main.log in root after first run

# For own development use virtualEnv

Guide is here http://docs.python-guide.org/en/latest/dev/virtualenvs/

Notice that /bin/ is /Scripts/ on Windows so to activate the virtual env use

```
source Scripts/activate
```

```python
py setup.py develop # installs depenencies
py setup.py sdist   # packages into zip
py setup.py compile # compiles readme.md to readme.html
py setup.py clean   # cleans root from install filesl ike .egg-info folder and such
```

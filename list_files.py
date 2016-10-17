#!/usr/bin/python3

import httplib2 # for Http
import os.path # for expanduser
import argparse # for ArgumentParser
import sys # for stderr
import apiclient.discovery # for build
import oauth2client.tools # for argparser
import oauth2client.file # for Storage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

CLIENT_SECRET_FILE = os.path.expanduser('~/.myworld/client_id.json')
APPLICATION_NAME = 'myworld'

def load_credentials():
    credential_path=os.path.expanduser('~/.credentials/myworld.json')
    if not os.path.isfile(credential_path):
        print('credential file [{0}] is missing'.format(credential_path), file=sys.stderr)
        print('create it with setup_credentials.py', file=sys.stderr)
        sys.exit(1)
    return oauth2client.file.Storage(credential_path).get()

def main():
    flags = argparse.ArgumentParser(parents=[oauth2client.tools.argparser]).parse_args()

    credentials = load_credentials()
    http = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('drive', 'v3', http=http)

    results = service.files().list(pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    while items:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    main()

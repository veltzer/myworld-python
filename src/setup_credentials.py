#!/usr/bin/python3

import os.path # for expanduser, join, isfile
import os # for mkdir
import argparse # for ArgumentParser
import sys # for stderr, exit
import oauth2client.file # for Storage
import oauth2client.tools # for run_flow, argparser
import oauth2client.client # for flow_from_clientsecrets

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

CLIENT_SECRET_FILE = os.path.expanduser('~/.myworld/client_id.json')
APPLICATION_NAME = 'myworld'

def create_new_creds(flags):
    flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    credentials = oauth2client.tools.run_flow(flow, store, flags)

def setup_credentials(flags):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = os.path.expanduser('~/.credentials/myworld.json')
    if os.path.isfile(credential_path):
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            create_new_creds(flags)
            print('Storing credentials to ' + credential_path)
        else:
            print(f'you already have valid credentials in [{credential_path}]...', file=sys.stderr)
            print('refusing to overwrite the credentials', file=sys.stderr)
            print('remove them if you want to recreate them...', file=sys.stderr)
            sys.exit(1)
    else:
        credential_dir = os.path.expanduser('~/.credentials')
        if not os.path.exists(credential_dir):
            os.mkdir(credential_dir)
        create_new_creds(flags)
        print('Storing credentials to ' + credential_path)


def main():
    flags = argparse.ArgumentParser(parents=[oauth2client.tools.argparser]).parse_args()
    setup_credentials(flags)


if __name__ == '__main__':
    main()

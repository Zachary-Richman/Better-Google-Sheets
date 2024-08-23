from googleapiclient import discovery
from google.oauth2 import service_account
import os


class Generation:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    def new_worksheet(self, sheet_name) -> str:
        """
        Creates a new worksheet in the given spreadsheet_id.
        :param sheet_name:
        :return: sheet_id (str)
        """
        if os.path.exists('service-account.json'):
            creds = service_account.Credentials.from_service_account_file('service-account.json')
        else:
            raise FileNotFoundError('Service account file not found.')

        service = discovery.build('sheets', 'v4', credentials=creds)

        request_body = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": sheet_name
                        }
                    }
                }
            ]
        }

        response = service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=request_body
        )

        return response.execute()
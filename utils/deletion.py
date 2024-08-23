from googleapiclient import discovery
from google.oauth2 import service_account
import os
from utils.reading import Reading


class Deletion:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    def delete_worksheet(self, sheet_name=None, sheet_id=None) -> str:
        """
        Creates a new worksheet in the given spreadsheet_id.
        :param sheet_id:
        :param sheet_name:
        :return: sheet_id (str)
        """
        if sheet_id and sheet_name is None:
            raise ValueError('You must specify a sheet name or ID.')
        elif sheet_id and sheet_id is not None:
            raise ValueError('You must cannot specify a sheet name and an ID.')

        reading_class = Reading(self.spreadsheet_id)
        if sheet_name is not None:
            sheet_id = reading_class.sheetname_to_id(sheet_name)

        if os.path.exists('service-account.json'):
            creds = service_account.Credentials.from_service_account_file('service-account.json')

        service = discovery.build('sheets', 'v4', credentials=creds)

        request_body = {
            "requests": [
                {
                    "deleteSheet": {
                        "sheetId": sheet_id
                    }
                }
            ]
        }

        response = service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=request_body
        )

        return response.execute()


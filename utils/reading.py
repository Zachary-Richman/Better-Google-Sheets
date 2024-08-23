from googleapiclient import discovery
from google.oauth2 import service_account
import os


class Reading:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    def sheetname_to_id(self, sheetname: str) -> str:
        """
            Retrieve the sheet ID for a given sheet name in the specified spreadsheet.

            :param sheetname: The name of the sheet to find.
            :return: The ID of the sheet if found; otherwise, None.
        """
        creds = service_account.Credentials.from_service_account_file('service-account.json')
        service = discovery.build('sheets', 'v4', credentials=creds)
        # Get the spreadsheet metadata
        spreadsheet = service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
        # Iterate through sheets to find the matching sheet name
        for sheet in spreadsheet.get('sheets', []):
            if sheet['properties']['title'] == sheetname:
                return sheet['properties']['sheetId']

    def read_sheet(self, sheetname=None, sheet_id=None, range_=None):
        if sheet_id and sheetname is None:
            raise ValueError('You must specify a sheet name or ID.')
        elif sheet_id and sheet_id is not None:
            raise ValueError('You must cannot specify a sheet name and an ID.')

        credentials = service_account.Credentials.from_service_account_file('service-account.json')
        service = discovery.build('sheets', 'v4', credentials=credentials)

        if sheetname:
            sheet_id = sheetname
        if range_ is None:
            range_ = sheet_id

        request = service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=range_)
        return request.execute()

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

    def read_sheet(self, sheet_id, range_=None):
        credentials = service_account.Credentials.from_service_account_file('service-account.json')
        service = discovery.build('sheets', 'v4', credentials=credentials)

        if range_ is None:
            range_ = sheet_id

        request = service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=range_)
        return request.execute()

    def read_row(self, row_num: int, sheet_id) -> list:
        worksheet = self.read_sheet(sheet_id)['values']
        if len(worksheet) > row_num:
            return worksheet[row_num]
        raise ValueError('Row num provided exceeds provided worksheet range.')

    def tables_to_dict(self, key_column, sheet_id) -> dict:
        worksheet = self.read_sheet(sheet_id)['values'][1:]

        temp_: dict = {}
        for row in worksheet:
            key = row[key_column]
            row_data = row[:key_column] + row[key_column + 1:]
            temp_[key] = row_data
        print(temp_)

    def get_by_keyword(self, keyword: str or list, sheet_id):
        worksheet = self.read_sheet(sheet_id)['values'][1:]

        returned_data = []
        if isinstance(keyword, list):
            for row in worksheet:
                if any(kw in row for kw in keyword):
                    returned_data.append(row)
        else:
            for row in worksheet:
                if keyword in row:
                    returned_data.append(row)

        return returned_data

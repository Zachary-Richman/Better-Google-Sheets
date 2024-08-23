class Conditionals:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    def highlighting(self, condition: str, condition_type: str, highlight_color: list or str, range_: str):
        """
        Highlights colors conditionally based off of things
        :param condition_type: [greaterthan, equalto, lessthan]
        :param range_: Range in the sheet
        :param condition:
        :param highlight_color:
        :return:
        """

        valid_conditions = ['greaterthan', 'equalto', 'lessthan']
        condition_type = condition_type.lower()  # Converts to lowercase to prevent capitalization errors

        if condition_type not in valid_conditions:
            raise ValueError(f'Condition type must be one of {valid_conditions}')

        if condition_type == 'greaterthan':
            
Better Google Sheets

The Better Google Sheets library provides the easiest and simplest way to interact with google sheets inside of Python.

## Getting Started
`pip install -r bgs_requirements.txt`

## Google Service Account
- Go to the [Google Cloud Console](https://www.console.cloud.google.com)
- Click on `IAM & Admin`
- Click on `Service Accounts` then `Create Service Account`
- Create your service account. Save the account email, and provide it **edit** access on your google sheet
- After creating the account, click on the email.
- Click on `Keys` in the topnav bar
- Then `ADD KEY` and then create a new key as JSON.
- Add it to your root directory and rename it `service-account.json`

## Usage
```python
from utils.generation import Generation
from utils.reading import Reading
from utils.deletion import Deletion
from utils.conditionals import Conditionals

bgs_gen = Generation('<spreadsheet_id>')
bgs_read = Reading('<spreadsheet_id>')
bgs_del = Deletion('<spreadsheet_id>')
bgs_cond = Conditionals('<spreadsheet_id>')

bgs_gen.create_worksheet(sheetname='My Sheet!')
# It's really that simple.
```

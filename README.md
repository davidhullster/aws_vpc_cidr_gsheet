## Description
script retrieves the list of VPCs using the describe_vpcs() method of the 
boto3 library, and then iterates through the list of VPCs and writes the CIDR 
for each VPC to the Google sheet using the append_row() method of the gspread library.

## Development
you will need a json file with google api credentials for a service account to use this file, and an appropriately named Google Sheet. The Google Drive and Google Docs api's must be enabled in your Google Developer account. The service account email must be added as a contributor to the Google Sheet.

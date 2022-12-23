"""
This script assumes that you have a Google sheet with the name "My Sheet" 
and that you have a credentials.json file in the same directory that contains 
the credentials for the Google Sheets API.

The script retrieves the list of VPCs using the describe_vpcs() method of the 
boto3 library, and then iterates through the list of VPCs and writes the CIDR 
for each VPC to the Google sheet using the append_row() method of the gspread library.
"""
import boto3
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Create an EC2 client
ec2 = boto3.client('ec2')

# Call the describe_vpcs() method to get a list of VPCs
vpcs = ec2.describe_vpcs()

# Set up credentials for the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_cred.json', scope)

# Create a client for the Google Sheets API
gs = gspread.authorize(credentials)

# Open the Google sheet and get the first worksheet
sheet = gs.open('20221223-VPC-CIDR').sheet1
account_name = 'dev-account'
vpc_region = 'us-east-1'
# Iterate through the list of VPCs and write the CIDR for each VPC to the Google sheet
sheet.clear()
sheet.update('A1', [['Account']])
sheet.update('B1', [['Region']])
sheet.update('C1', [['VPC Name']])
sheet.update('D1', [['CIDR']])
sheet.format('A1:D1', {'textFormat': {'bold': True}})
for vpc in vpcs['Vpcs']:
    for tag in vpc['Tags']:
        if tag['Key'] == "Name":
            vpc_name = [tag['Value']]
        sheet.append_row([account_name] + [vpc_region] + vpc_name + [vpc['CidrBlock']])

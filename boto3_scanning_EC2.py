import boto3

aws_dev_console = boto3.session.Session(profile_name="devs")
my_custom_ec2s = boto3.client('ec2')
total_regions = my_custom_ec2s.describe_regions()
for regionList in total_regions['Regions']:
    print(regionList)

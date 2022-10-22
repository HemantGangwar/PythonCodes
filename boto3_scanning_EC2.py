import boto3

aws_dev_console = boto3.session.Session(profile_name="mypc")
my_custom_ec2s = boto3.client('ec2')
total_regions = my_custom_ec2s.describe_regions()

total_regions_count = len(total_regions['Regions'])
for regionList in total_regions['Regions']:
    region_Marker = regionList['RegionName']
    print('EC2 contained within: ', region_Marker)
    my_custom_ec2s = boto3.client('ec2', region_name = region_Marker)
    instances = my_custom_ec2s.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
              print("Instance ID: ", instance['InstanceId'], "," ,"Instance Name: ", instance['Tags'][0]['Value'])
#              x = instance['Tags'][0]['Value']
#              print(x)


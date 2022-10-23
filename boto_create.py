import boto3

# Let's create an EC2 resource

cutom_region = input('''Enter the region where you want to deploy? 
                        ap-south-1
                        eu-west-2
                        eu-north-1
                        us-east-1
                        
_: ''') 

aws_dev_console = boto3.session.Session(profile_name="mypci")
my_custom_ec2 = aws_dev_console.resource('ec2', region_name = cutom_region)

if cutom_region == 'ap-south-1':
    relevantAMI = "ami-00a2ea0777b445307"
    relevantHaredware = "t2.micro"
    relevantKey = "Windows-Key-2022"
    relevantSGList = ["sg-042d32b5ca9656061"]
    relevantAZ = "ap-south-1a"
elif cutom_region == 'eu-west-2':
    relevantAMI = "ami-06db9d8fca38be745"
    relevantHaredware = "t2.micro"
    relevantKey = "AWS-Key-Pair-London"
    relevantSGList = ["sg-0ab61b7b1867fe0fd"]
    relevantAZ = "eu-west-2b"   
elif cutom_region == 'eu-north-1':
    relevantAMI = "ami-08870b363a0fbb474"
    relevantHaredware = "t3.micro"
    relevantKey = "AWS-Key-Pair-Stockholm"
    relevantSGList = ["sg-0ae04aed4ebd7b5c9"]
    relevantAZ = "eu-north-1c"
elif cutom_region == 'us-east-1':
    relevantAMI = "ami-0f1ee03d06c4c659c"
    relevantHaredware = "t2.micro"
    relevantKey = "AWS-Key-Pair-Virginia"
    relevantSGList = ["sg-0e813c406dfde95d5"]
    relevantAZ = "us-east-1a"
else:
    print('No relevant region found, exiting !!!')
    quit() 

instances = my_custom_ec2.create_instances(
        ImageId = relevantAMI,
        MinCount=1,
        MaxCount=1,
        InstanceType=relevantHaredware,
        KeyName=relevantKey,
        SecurityGroupIds=relevantSGList,
        Placement={
            'AvailabilityZone': relevantAZ,
            'Tenancy': 'default',
            },
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': input('Enter custom EC2 name ? ')
                },
            ]
        },
        ],
        )

print(instances)

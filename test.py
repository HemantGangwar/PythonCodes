import boto3

aws_dev_console = boto3.session.Session(profile_name="devs")

x = dir(aws_dev_console)

ec2_ops = aws_dev_console.resource('ec2', region_name = "ap-south-1")

print(dir(ec2_ops))

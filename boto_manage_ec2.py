
import boto3

# Let's Fetch details of region

my_custom_region = input("Enter the region which you wish to work upon ? ")

my_custom_ec2 = boto3.client('ec2', region_name = my_custom_region)

# Defining EC2 function
def ec2CustomFunction(requestedaction, inputEC2):
    if requestedaction == 'stop':
        action_response = my_custom_ec2.stop_instances(InstanceIds=inputEC2)
    elif requestedaction == 'start':
        action_response = my_custom_ec2.start_instances(InstanceIds=inputEC2)
    elif requestedaction == 'terminate':
        action_response = my_custom_ec2.terminate_instances(InstanceIds=inputEC2)
    else:
        print("Undefined Option, exiting the Program !!!")
        quit()

    return action_response

instances = my_custom_ec2.describe_instances()
for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'], "," ,instance['State'])

# Terminating a particular instance

ec2_action_Decision = input('Please confirm if you want to perform any actions on EC2 (y / n) ? ').lower()
if ec2_action_Decision == 'y':
    ec2_operation_Action = input('Enter Action you want to perform (start, stop, terminate): ').lower()
    detail_of_Instance = input('Enter the name of the instance: ')
    test_list = []
    test_list.append(detail_of_Instance)
    if ec2_operation_Action == 'stop':
        response = ec2CustomFunction('stop', test_list)
    elif ec2_operation_Action == 'start':
        response = ec2CustomFunction('start', test_list)
    elif ec2_operation_Action == 'terminate':
        response = ec2CustomFunction('terminate', test_list)
    else:
        print('Bye !!!')
else:
    quit()

print(response)

    

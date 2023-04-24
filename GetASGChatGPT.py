import boto3

# create a CloudFormation client
cf_client = boto3.client('cloudformation')

# get the stack name from the user
stack_name = input("Enter the name of the CloudFormation stack: ")

# describe the stack to get its input parameters
stack = cf_client.describe_stacks(StackName=stack_name)['Stacks'][0]

# loop through the input parameters to find the ASG group name
asg_group_name = None
for param in stack['Parameters']:
    if param['ParameterKey'] == 'ASGGroupName':
        asg_group_name = param['ParameterValue']
        break

# print the ASG group name (if found)
if asg_group_name:
    print(f"The ASG group name is {asg_group_name}.")
else:
    print("No ASG group name found in stack inputs.")

import boto3

# Replace with the name of your CloudFormation stack
stack_name = 'my-cloudformation-stack'

# Create a CloudFormation client
cf_client = boto3.client('cloudformation')

# Get the physical resource ID of the ASG created by the stack
response = cf_client.describe_stack_resources(
    StackName=stack_name,
    LogicalResourceId='MyAutoScalingGroup'  # Replace with the logical resource ID of your ASG
)
asg_id = response['StackResources'][0]['PhysicalResourceId']

# Create an Auto Scaling client
asg_client = boto3.client('autoscaling')

# Update the Launch process for the ASG
asg_client.resume_processes(
    AutoScalingGroupName=asg_id,
    ScalingProcesses=['Launch']
)

import boto3
import os
import time

Stack= input("enter stack name: ")
ASG= $(aws cloudformation describe-stack-resources --stack-name $Stack --query 'StackResources[?ResourceType==`AWS::AutoScaling::AutoScalingGroup`].PhysicalResourceId' --output text)
print(ASG)

client = boto3.client('autoscaling')
response = client.suspend_processes(
    AutoScalingGroupName='test',
    ScalingProcesses=[
        'Launch','Terminate',
    ],
)

print(response)

import boto3
import os
import time

client = boto3.client('autoscaling')
response = client.resume_processes(
    AutoScalingGroupName='test',
    ScalingProcesses=[
        'Launch','Terminate',
    ],
)

print(response)

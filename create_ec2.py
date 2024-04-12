import boto3

#Set up EC2 client
ec2 = boto3.client('ec2')

#Specify instance parameters
image_id = 'ami-0557q15b87f6559cf'
instance_type = 't2.micro'
key_name = 'Wordpress'
security_group_ids = ['sg-0e4d813ab0f821b1e']
subnet_id = 'subnet_b40f1df9'

#Launch EC2 instance
response = ec2.run_instances(ImageId=image_id, InstanceType=instance_type, KeyName=key_name, MaxCount=1

#Get instanceID from response
instance_id = response['Instances'][0]['InstanceId']

#Wait for instance to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

#Print instance information
instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
print(f"Instance ID : {instance_id}")
print(f"Public IP Address : {instance.get('PublicIpAddress','N/A')}")
print(f"Private IP Address : {instance.egt('PrivateIpAddress','N/A')}")

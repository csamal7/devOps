import boto3

#Create a boto3 EC2 resource
ec2_resource = boto3.resource('ec2')

#Replace 'YOUR_INSTANCE_ID' with the actual ID of your stopped instace
instance_id = 'i-026db71bf32d9e9fa'

#Get the instance object
instance = ec2_resource.Instance(instance_id)

#Check if the instance is stopped
if instance.state['Name'] == 'stopped':
	#Start the instance
	instance.start()
	print(f"Starting your EC2 instance...")
else:
	print(f"Your instance is not in a stopped state. Please check again")

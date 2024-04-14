import boto3

#Create a boto3 EC2 resource
ec2_resource = boto3.resource('ec2')

#Replace 'YOUR_INSTANCE_ID' with the actual ID of the instance you want to stop
instance_id = input("Enter the instance_id that needs to be stopped : ")

#Get the instance object
instance = ec2_resource.Instance(instance_id)

#Check if the instance is stopped
if instance.state['Name'] == 'running':
        #Stopping the instance
        instance.stop()
        print(f"Stop your EC2 instance...")
else:
        print(f"Your instance is already in a stopped state. Please check again")

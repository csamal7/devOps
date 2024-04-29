#!/bin/bash

#############################################
# Author CS				    #
# Date 4/1/2024				    #
#					    #
# Version v1				    #
# This script reports AWS resource usage    #
#############################################


# AWS S3
# AWS EC2
# AWS Lambda
# AWS IAM users

# list S3 buckets
echo "Print list of s3 buckets"
aws s3 ls

# list EC2 instances
echo "Print list of ec2 instanes"
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'

# list lambda
echo "Print list of lambda functions"
aws lambda list-functions

# list of IAM users
echo "Print list of IAM users"
aws iam list-users

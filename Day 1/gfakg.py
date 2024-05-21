import boto3
ec2 = boto3.resource('ec2',
                    'ap-south-1',
                     aws_access_key_id='',
                     aws_secret_access_key='',
                     )
instance = ec2.create_instances(InstanceType='t2.micro',
                                ImageId='',
                                MaxCount=1,
                                MinCount=1)
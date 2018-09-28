#!/usr/bin/python
import boto3
import json

#use the client
ec2=boto3.client('ec2', region_name="ap-south-1")

#List all the SG in region
response=ec2.describe_security_groups()

#print json.dumps(response)

for SGs in response["SecurityGroups"]:
#Filter
#    print SGs["GroupId"]
    for rules in SGs["IpPermissions"]:
        if (rules["IpProtocol"] == "tcp" and rules["FromPort"] == 22):
            #print SGs["GroupId"]

##to remove IPv4
            for cidr in rules["IpRanges"]:
                if ( cidr["CidrIp"] == "0.0.0.0/0" ):
                    print "Hello"
                    sgresponse=ec2.revoke_security_group_ingress(CidrIp="0.0.0.0/0",GroupId=SGs["GroupId"],FromPort=22,IpProtocol="tcp",ToPort=22)
                    print sgresponse

##to remove IPv6
            for cidr6 in rules["Ipv6Ranges"]:
                if ( cidr6["CidrIpv6"] == "::/0" ):
                    print "Hello"
                    sgresponse=ec2.revoke_security_group_ingress(GroupId=SGs["GroupId"],IpPermissions=[{'FromPort': 22,'ToPort': 22, 'IpProtocol': 'tcp', 'Ipv6Ranges': [ { 'CidrIpv6': '::/0' }, ] }])
                    print sgresponse

#!/usr/bin/python

import boto
import boto.s3.connection

#Enter AWS Access Key and Secret Key
access_key = ''
secret_key = ''

#Set Object Expiration Time, ex: max-age=60
objexp = '' 

#Enter Bucket Name
s3bucket = ''

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        )
b = conn.get_bucket(s3bucket)

#Add Cache-Control to each object if it doesn't exist
for key in b.list():
        k = b.get_key(key)

        if k.cache_control!=objexp:
                b.copy_key(key.name,s3bucket,key.name,metadata={'Content-Type': k.content_type, 'Cache-Control': objexp})

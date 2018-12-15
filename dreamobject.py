import os

import boto

conn = boto.connect_s3(host='objects-us-east-1.dream.io')

bucket = conn.get_bucket('mechmotum')

assets_dir = 'assets'

files = os.listdir(assets_dir)

for fname in files:
    print('Uploading {}'.format(fname))
    key = boto.s3.key.Key(bucket, fname)
    key.set_contents_from_filename(os.path.join(assets_dir, fname))

for o in bucket.list():
    o.set_acl('public-read')

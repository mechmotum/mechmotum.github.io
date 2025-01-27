# Create a ~/.boto file with:
#[Credentials]
#aws_access_key_id = <key>
#aws_secret_access_key = <key>

import os

import boto3
import botocore

accepted_file_exts = ['.pdf', '.png', '.gif', '.mp4', '.jpg', '.svg']
BUCKET_NAME = 'mechmotum'
HOST = 'objects-us-east-1.dream.io'
assets_dir = 'assets'


def upload(overwrite=False):

    s3 = boto3.resource('s3')
    s3client = boto3.client('s3')
    bucket = s3.Bucket(BUCKET_NAME)

    files = os.listdir(assets_dir)

    for fname in files:
        if os.path.splitext(fname)[-1] in accepted_file_exts:
            #key = conn.Object(bucket, fname)
            try:
                key = s3.Object(bucket, fname)
                #key.load()
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    # The key does not exist.
                    print('The key does not exist.')
                elif e.response['Error']['Code'] == 403:
                    # Unauthorized, including invalid bucket
                    print('Unauthorized, including invalid bucket')
                else:
                    # Something else has gone wrong.
                    print('Something went wrong, this is just a test.')
                    raise 
            
            s3.Object(BUCKET_NAME, fname).put(Body=open(os.path.join(assets_dir, fname), 'rb'))
        else:
            print('Skipping: {}'.format(fname))

    for o in bucket.list():
        o.Acl().put(ACL='public-read')


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Upload Files to Dreamhost.')
    parser.add_argument('--overwrite', action='store_true',
                        help="Forces files to be overwritten.")
    args = parser.parse_args()

    upload(overwrite=args.overwrite)

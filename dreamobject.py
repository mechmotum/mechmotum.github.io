# Create a ~/.aws/credentials file with:
#[Credentials]
#aws_access_key_id = <key>
#aws_secret_access_key = <key>

import os

import boto3
from botocore.exceptions import ClientError

accepted_file_exts = ['.pdf', '.png', '.gif', '.mp4', '.jpg', '.svg']
BUCKET_NAME = 'mechmotum'
HOST = 's3.us-east-005.dream.io'
assets_dir = 'assets'


def upload(overwrite=False):

    session = boto3.session.Session()
    s3 = session.resource('s3', endpoint_url=f'https://{HOST}')
    bucket = s3.Bucket(BUCKET_NAME)

    files = os.listdir(assets_dir)

    for fname in files:
        if os.path.splitext(fname)[-1] in accepted_file_exts:
            s3_object = bucket.Object(fname)
            try:
                s3_object.last_modified
            except ClientError:
                print('Uploading: {}'.format(fname))
                s3_object.upload_file(os.path.join(assets_dir, fname))
                s3_object.Acl().put(ACL='public-read')
            else:
                if overwrite is False:
                    msg = 'Skipping: {} (already present in the bucket)'
                    print(msg.format(fname))
                else:
                    print('Overwriting, uploading: {}'.format(fname))
                    s3_object.upload_file(os.path.join(assets_dir, fname))
                    s3_object.Acl().put(ACL='public-read')


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Upload Files to Dreamhost.')
    parser.add_argument('--overwrite', action='store_true',
                        help="Forces files to be overwritten.")
    args = parser.parse_args()

    upload(overwrite=args.overwrite)

# Create a ~/.boto file with:
#[Credentials]
#aws_access_key_id = <key>
#aws_secret_access_key = <key>

import os

import boto

accepted_file_exts = ['.pdf', '.png', '.gif', '.mp4', '.jpg', '.svg']
BUCKET_NAME = 'mechmotum'
HOST = 'objects-us-east-1.dream.io'
assets_dir = 'assets'


def upload(overwrite=False):

    conn = boto.connect_s3(host=HOST)
    bucket = conn.get_bucket(BUCKET_NAME)

    files = os.listdir(assets_dir)

    for fname in files:
        if os.path.splitext(fname)[-1] in accepted_file_exts:
            key = boto.s3.key.Key(bucket, fname)
            if key.exists() and overwrite is False:
                msg = 'Skipping: {} (already present in the bucket)'
                print(msg.format(fname))
            else:
                print('Uploading: {}'.format(fname))
                key.set_contents_from_filename(os.path.join(assets_dir, fname))
        else:
            print('Skipping: {}'.format(fname))

    for o in bucket.list():
        o.set_acl('public-read')


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Upload Files to Dreamhost.')
    parser.add_argument('--overwrite', action='store_true',
                        help="Forces files to be overwritten.")
    args = parser.parse_args()

    upload(overwrite=args.overwrite)

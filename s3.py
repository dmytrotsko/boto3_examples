import boto3
from botocore.exceptions import ClientError
from typing import Optional


class S3Bucket:
    def __init__(self):
        self.s3 = boto3.resource("s3")

    def create_bucket(self, bucket_name: str, region: Optional[str] = None):
        """Create bucket with given name in specified region.
        If region was not specified, the bucket will be created in default region which is set to `us-east-1`

        Args:
            bucket_name (str): Desired bucket name. Bucket name should be globaly unique.
            region (Optional[str], optional): Region to create bucket in. Defaults to None which means that Bucket will be created in default region `us-east-1`.
        Return:
            True: bucket is created
            False: bucket was not created (check `e` to see why).
        """

        try:
            if region is None:
                self.s3.create_bucket(Bucket=bucket_name)
            else:
                location = {"LocationConstraint": region}
                self.s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        except ClientError as e:
            print(e)
            return False
        return True

    def list_all_buckets(self):
        """List all buckets"""
        for bucket in self.s3.buckets.all():
            print(bucket.name)

    def delete_bucket(self, bucket_name: str):
        """Delete bucket by name

        Args:
            bucket_name (str): S3 Bucket name
        """
        self.s3.delete_bucket(Bucket=bucket_name)
        print(f"S3 bucket deleted successfully: {bucket_name}")

    def list_bucket_objects(self, bucket_name: str):
        """List all objects in bucket with `bucket_name`

        Args:
            bucket_name (str): S3 Bucket name
        """
        response = self.s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in response:
            for obj in response["Contents"]:
                print(obj["Key"])
        else:
            print("No objects found in the bucket.")

    def upload_file(self, local_file_path: str, bucket_name: str, s3_key: str):
        """Upload file to S3 Bucket

        Args:
            local_file_path (str): Local path to the file to upload
            bucket_name (str): S3 Bucket name
            s3_key (str): Desired file name
        """
        self.s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3 bucket: {bucket_name}")

    def download_file(self, bucket_name: str, s3_key: str, local_file_path: str):
        """Download file from S3 Bucket

        Args:
            bucket_name (str): S3 Bucket name
            s3_key (str): File name to download
            local_file_path (str): Local path to save file
        """
        self.s3.download_file(bucket_name, s3_key, local_file_path)
        print(f"File downloaded successfully to: {local_file_path}")

    def delete_file(self, bucket_name: str, s3_key: str):
        """Delete file

        Args:
            bucket_name (str): S3 Bucket name
            s3_key (str): Name of file to delete
        """
        self.s3.delete_object(Bucket=bucket_name, Key=s3_key)
        print(f"File deleted successfully from S3 bucket: {bucket_name}")

    def find_by_prefix(self, prefix: str):
        """Find files by prefix

        Args:
            prefix (str): File prefix
        """
        for bucket in self.s3.buckets.all():
            for obj in bucket.objects.filter(Prefix=f"{prefix}/"):
                print(f"{bucket.name}, {obj.key}")

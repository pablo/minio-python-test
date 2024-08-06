from minio import Minio

from config import ACCESS_KEY, SECRET_KEY


def main():

    client = Minio("192.168.16.24:9000",
        secure=False,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY
    )

    # The file to upload, change this path if needed
    source_file = "test.jpg"

    # The destination bucket and filename on the MinIO server
    bucket_name = "backyardigans"
    destination_file = "test.jpg"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("Error ocurred.", exc)




import csv
# import boto3
#
with open("credentials.csv","r") as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]

# client=boto3.client("rekognition",aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
# response=client.compare_faces(
#     {
#         SourceImage={
#     'S3Object':{
#         'Bucket':'suspectfaces',
#         'Name':''
#     }
# },
#         TargetImage={
#     'S3Object':{
#         'Bucket':'suspectfaces'
#         'Name':''
#     }
# },
#     }
# )
#
# import csv
# import boto3
#
# with open("credentials.csv","r") as input:
#     next(input)
#     reader=csv.reader(input)
#     for line in reader:
#         access_key_id=line[2]
#         secret_access_key=line[3]
#
# photo="first.jpeg"
#
# client=boto3.client("rekognition",aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
# response=client.compare_faces(
#     {
#         SourceImage={
#     'S3Object':{
#         'Bucket':'suspectfaces',
#         'Name':''
#     }
# },
#         TargetImage={
#     'S3Object':{
#         'Bucket':'suspectfaces'
#         'Name':''
#     }
# },
#     }
# )
#
import boto3
source_img = 'third.jpeg'
ss=boto3.client('s3',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
ss.upload_file(source_img, 'suspectfaces',source_img)



client = boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
s3 = boto3.resource('s3',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
my_bucket = s3.Bucket('suspectfaces')





detected_faces=[]

for my_bucket_object in my_bucket.objects.all():
    print("==========="+my_bucket_object.key+"===============")
    if(source_img!=my_bucket_object.key):
        response = client.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': 'suspectfaces',
                    'Name': source_img
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': 'suspectfaces',
                    'Name': my_bucket_object.key
                }
            }
        )
        print(response)
        if(len(response["FaceMatches"])):
            detected_faces.append((my_bucket_object.key,response["FaceMatches"][0]["Similarity"]))
        print(response["FaceMatches"])
        print("==========================")

print(detected_faces)

s3 = boto3.resource('s3',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
s3.Object("suspectfaces", source_img).delete()
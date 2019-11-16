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

client = boto3.client('rekognition')
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('police-hack')

source_img = 'person3.jpg'
detected_faces=[]

for my_bucket_object in my_bucket.objects.all():
    print("==========="+my_bucket_object.key+"===============")
    if(source_img!=my_bucket_object.key):
        response = client.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': 'police-hack',
                    'Name': source_img
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': 'police-hack',
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
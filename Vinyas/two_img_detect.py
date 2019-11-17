import boto3
import csv

with open("credentials.csv","r") as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]


if __name__ == "__main__":

    # Replace sourceFile and targetFile with the image files you want to compare.
    sourceFile = 'appasaheb1.jpg'
    targetFile = 'test.jpeg'
    client = boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=70,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + confidence + '% confidence')

    imageSource.close()
    imageTarget.close()
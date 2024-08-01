import cv2
import os
noofmask=0
noofnomask=0
import mysql.connector as sqlcon
a=sqlcon.connect(host="localhost",user="root",password="0000",data
base="facialrecognition")
c=a.cursor()
if a.is_connected():
 print("saved to database")
else:
 print("Oops! data not saved")
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata,
AnalyzeEnums
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey='WSOSBYcXd24IZ-Oat69RDsyQvR1mOFZcJQy_YN7Y0ZPS'
url='https://api.us-south.visualrecognition.watson.cloud.ibm.com/instances/13e033bc-8145-465b887e-a2631a4ffd16'
collection='2c6bee88-97a0-4503-ac2b-f47c19261107'
authenticator = IAMAuthenticator(apikey)
service = VisualRecognitionV4('2018-03-19',
authenticator=authenticator)
service.set_service_url(url)
def loadImages(path="."):
 return [os.path.join(path,f)for f in os.listdir(path) if f.endswith('.jpg')]
filenames=loadImages()
for i in filenames:
 with open(i, 'rb') as mask_img:
 analyze_images =
service.analyze(collection_ids=[collection],features=[AnalyzeEnums.Fea
tures.OBJECTS.value],images_file=[FileWithMetadata(mask_img)]).get_
result()
 obj =
analyze_images['images'][0]['objects']['collections'][0]['objects'][0]['obj
ect']
 if obj=="mask":
 noofmask=noofmask+1
 else:
 noofnomask=noofnomask+1
 c.execute("insert into imgdata values('{}','{}')".format(i,obj))
print("no of photos with mask:-",noofmask)
print("no of photos without mask:-",noofnomask)
a.commit()
 

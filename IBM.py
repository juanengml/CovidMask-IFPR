import json
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from datetime import datetime
import cv2

class Model(object):
    def __init__(self,frame,api_key,model_id):
        self.frame = frame
        self.api_key = api_key
        self.model_id = model_id
        self.authenticator = IAMAuthenticator(self.api_key)
        self.visual_recognition = VisualRecognitionV4(
              version='2019-02-11',
              authenticator=self.authenticator
         )
        self.visual_recognition.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?')

    def label_predict(self):
         with open(self.frame, 'rb') as honda_file:
            result = self.visual_recognition.analyze(
                collection_ids=[self.model_id],
                features=[AnalyzeEnums.Features.OBJECTS.value],
                images_file=[
                    FileWithMetadata(honda_file)],
                threshold=0.20
                    ).get_result()
            return result['images'][0]['objects']['collections'][0]['objects']

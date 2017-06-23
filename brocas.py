import requests

class Brocas(object):
    def textToSpeech(self, text):      
        payload = {"text": text}
        
        response = requests.post("http://localhost:5002", json=payload)

        return response.text
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('i-r5O-zDXsl77SM0-VtWlcyid_cTP1BNm1Vx18rGFEc4')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b70fd758-36d8-429b-95f3-d549fa3f28e1')

def english_to_french(english_text):
    french_translation = language_translator.translate(
        text=english_text,
        model_id = "en-fr").get_result()
    return french_translation['translations'][0]['translation']

def french_to_english(french_text):
    english_translation = language_translator.translate(
        text=french_text,
        model_id = "fr-en").get_result()
    return english_translation['translations'][0]['translation']

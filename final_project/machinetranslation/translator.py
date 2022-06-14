import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
 
load_dotenv()
 
apikey = os.environ['apikey']
url = os.environ['url']
 
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 
authenticator = IAMAuthenticator('WVT-eP3h00U3cnEbxUrJZKVwsSv2tUtdLSnRZJcQ2E0S')
language_translator = LanguageTranslatorV3(
    version='6.0.0',
    authenticator=authenticator
)
 
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/56ccf5c8-38b4-4b6c-9f18-7c4e92a82768')
 
def english_to_french(english_text):
    """Translates English to French"""
    frenchtranslation = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    # return frenchtranslation
    return frenchtranslation["translations"][0]["translation"]
def french_to_english(french_text):
    """Transalates French to English"""
    englishtranslation = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    return englishtranslation["translations"][0]["translation"]
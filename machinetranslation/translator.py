import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-25',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Return French Translation from English Text"""
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()

    frenchText=str(translation['translations'][0]['translation'])
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frenchText

def frenchToEnglish(frenchText):
    """Return French Translation from English Text"""
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()

    englishText=str(translation['translations'][0]['translation'])
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return englishText
    
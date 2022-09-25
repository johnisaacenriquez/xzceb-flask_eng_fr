# Module to translate English to French and French to English
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# IBM Watson credentials
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)

# Language translator instance
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    # Translate English text to French text
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text.get('translations')[0].get('translation')

def french_to_english(french_text):
    # Translate French text to English text
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text.get('translations')[0].get('translation')

import requests
import os
from cryptography.fernet import Fernet

from constants.api import BASE_URL

def get(url, params = {}):
    encryptionKey = bytes(os.getenv('ENCRYPTION_KEY'), 'utf-8')
    encryptedApiKey = bytes(os.getenv('API_KEY'), 'utf-8')

    f = Fernet(encryptionKey)
    apiKey = f.decrypt(encryptedApiKey).decode('utf-8')

    defaultParams = {
        'apikey': apiKey,
    }

    defaultParams.update(params)

    try:
        response = requests.get(BASE_URL + url, params=defaultParams)

        response.raise_for_status()

        data = response.json()

        return data
    except:
        return None
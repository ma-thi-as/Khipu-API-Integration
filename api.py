import hashlib
import aiohttp
import asyncio
import json
import hmac
import os
from os.path import join, dirname
from dotenv import load_dotenv
from urllib.parse import quote_plus, quote, urlencode

##Debug
import time
import pdb

DOTENV_PATH = join(dirname(__file__), '.env.dev')
load_dotenv(DOTENV_PATH)

credentials = {
    "receiver_id" : os.environ.get('receiver_id'),
    "secret" : os.environ.get('secret')
}

def auth_configuration(url: str, method: str, secret: str, post_params: dict):
    # Formatear la url para reemplazar caracteres como *,+,etc
    formatted_url = quote(url, safe='', encoding=None, errors=None)
    # Concatenar el método con la url  METHOD_HTTP + & + KHIPU_URL_WITH_PERCENT_ENCODE 
    to_sign = method.upper() + "&" + formatted_url
    print(to_sign)
    if method == 'GET' or method == 'DELETE':
        # Generar hash HMAC-SHA256
        auth_hash = hmac.new(secret.encode('UTF-8'), to_sign.encode("UTF-8"), hashlib.sha256).hexdigest()
        return f"{credentials.get('receiver_id')}:{auth_hash}"

    if method == 'POST':
        if post_params:
            # Convertir los parámetros de la solicitud a una cadena codificada
            params_encoded = urlencode(post_params)
            # Construir la cadena para la firma incluyendo los parámetros de la solicitud
            data_to_sign = to_sign + '&' + params_encoded
            # Generar la firma HMAC-SHA256
            auth_hash = hmac.new(secret.encode('UTF-8'), data_to_sign.encode("UTF-8"), hashlib.sha256).hexdigest()
            return f"{credentials.get('receiver_id')}:{auth_hash}"

def params_sorted(params:dict):
    sorted_params = {}
    #Ordenar por clave lexigraficamente
    for key in sorted(params): 
        sorted_params.setdefault(key,params[key])
    return sorted_params

def params_to_lowercase(params:dict):
    to_lower={}
    for k,v in params.items():
        to_lower.setdefault(str(k).lower(), str(v).lower())
    return to_lower

def required_params_is_present( params: dict, REQUIRED_PARAMS:list):
    for p in REQUIRED_PARAMS:
        if p not in params:
            return False
    return True

async def make_request(url: str, method: str, headers:dict, sorted_data: dict ):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, data=sorted_data, headers=headers) as response:
            return  await response.text() 


# Manager para realizar peticiones a la API de Khipu
async def requestManager(url: str, method: str, params: dict):
    sorted_params = params_sorted(params)
    headers = {
        'Authorization': auth_configuration(url=url, method=method, secret=credentials.get('secret'), post_params=sorted_params),
        'Content-Type': 'application/x-www-form-urlencoded'
        }

    # Ejecutar la solicitud y obtener el texto de respuesta
    response_text = await make_request(url=url, method=method, sorted_data=sorted_params, headers=headers)
    return response_text

def get_available_banks():
    method = "GET"
    url = "https://khipu.com/api/2.0/banks"
    params = {'receiver_id': credentials.get("receiver_id")}
    # Obtener el bucle de eventos
    loop = asyncio.get_event_loop()
    # Ejecutar la solicitud y obtener el texto de respuesta
    response_text = loop.run_until_complete(requestManager(url=url, method=method, params=params))
    # Devolver el texto de respuesta

#Falta mejorar e implementar parametros dinamicos
def make_payment(params:dict):
    method = "POST"
    url = "https://khipu.com/api/2.0/payments"
    REQUIRED_PARAMS = ["amount","currency","subject","transaction_id"]

    params = params_to_lowercase(params=params)
    params_present = required_params_is_present(params=params, REQUIRED_PARAMS=REQUIRED_PARAMS)
    
    loop = asyncio.get_event_loop()
    #Ejecutar la solicitud y obtener el texto de respuesta
    response_text = loop.run_until_complete(requestManager(url=url, method=method, params=params)) if params_present else None
    return response_text

def get_payment_by_id(payment_id:str):
    method = "GET" 
    url = f"https://khipu.com/api/2.0/payments/{payment_id}"
    params = params_to_lowercase({'payment_id':payment_id})
    REQUIRED_PARAMS = ["payment_id"]

    #check if required params exists in params
    params_present = required_params_is_present(params=params, REQUIRED_PARAMS=REQUIRED_PARAMS)
    
    loop = asyncio.get_event_loop()
    #Ejecutar la solicitud y obtener el texto de respuesta
    response_text = loop.run_until_complete(requestManager(url=url, method=method, params=params)) if params_present else None

    return response_text


def delete_payment(payment_id:str):
    method = "DELETE" 
    url = f"https://khipu.com/api/2.0/payments/{payment_id}"
    params = params_to_lowercase({'payment_id':payment_id})
    REQUIRED_PARAMS = ["payment_id"]

    #Si los params requeridos estan en los params
    params_present = required_params_is_present(params=params, REQUIRED_PARAMS=REQUIRED_PARAMS)
    #loop de eventos de la response
    loop = asyncio.get_event_loop()
    #Ejecutar la solicitud y obtener el texto de respuesta
    response_text = loop.run_until_complete(requestManager(url=url, method=method, params=params)) if params_present else None

    return response_text

## wait response of khpu
def confirm_payment(payment_id:int):
    method = "POST" 
    url = f"https://khipu.com/api/2.0/payments/{payment_id}/confirm"
    params = params_to_lowercase({'payment_id':payment_id})
    REQUIRED_PARAMS = ["payment_id"]

    #Si los params requeridos estan en los params
    params_present = required_params_is_present(params=params, REQUIRED_PARAMS=REQUIRED_PARAMS)
    #loop de eventos de la response
    loop = asyncio.get_event_loop()
    #Ejecutar la solicitud y obtener el texto de respuesta
    response_text = loop.run_until_complete(requestManager(url=url, method=method, params=params)) if params_present else None
    
    return response_text

#print(make_payment({"subject":"XDDD","currency":"CLP", "amount":"100","transaction_id":"XDASDAS"}))
#print(make_payment({"subject":"XDDD","currency":"CLP", "amount":"100","transaction_id":"XDASDAS","notify":"https://test.cl","notify_api_version":"1.3"}))
#print(get_payment_by_id(payment_id="pkxarwbko9uz"))



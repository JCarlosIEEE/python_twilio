from fastapi import APIRouter
from pydantic import BaseModel
from twilio.rest import Client
from fastapi import HTTPException, Request
from os import getenv

router = APIRouter()

class MensajeTexto(BaseModel) :
    Mensaje : str
    Celular : int

# Envio de mensajes a whatsapp
@router.post('/')
async def json_factura(cabecera: Request, factura: MensajeTexto):
    print(getenv('SECRET'))
    # Comprobamos que el header contiene los datos de autenticación
    if 'Authorization' not in cabecera.headers:
        raise HTTPException(status_code=400, detail={'error': 'No se encontró el header Authorization'})
    # Comprobamos que la llave de autenticación sea correcta
    if cabecera.headers['Authorization'].split(' ')[1] != getenv('SECRET'):
        raise HTTPException(status_code=400, detail={'error': 'La llave de autenticación no es correcta'})

    account_sid =''
    auth_token = ''
    client = Client(account_sid, auth_token)
    msg = ''' 
    *FACTURA DE COMPRA*
    *************************************************************************
    *Dirección*: {Mensaje}
    *Celular*: {Celular}

    *************************************************************************
    '''.format(**factura.dict())
                
    message = client.messages.create(
                            body= msg,
                            from_='whatsapp:+14155238886',#'+14344488907',#
                            to=f'whatsapp:+57{factura.Celular}'#'+573125599599'
                        )
    return {'respuesta': 'ok', 'status_server':200, 'mensaje': 'ENVIADO'}

''''
@router.post('/prueba')
async def prueba(mensaje: MensajeTexto):
    print(mensaje.Mensaje)
    return {'respuesta': 'ok', 'status_server':200, 'mensaje': 'ENVIADO'}'''



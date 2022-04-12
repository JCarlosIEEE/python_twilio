from fastapi import FastAPI

#from fastapi import APIRouter
from pydantic import BaseModel
from twilio.rest import Client
#from fastapi import HTTPException, Request
import os
#from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
#from boto.s3.connection import S3Connection
#s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])


app = FastAPI()

@app.get("/inicio")
async def root():
    return "Hello World!"

class MensajeTexto(BaseModel) :
    Mensaje : str
    Celular : int

# Envio de mensajes a whatsapp
@app.post('/factura')
async def json_factura(factura: MensajeTexto):

    account_sid = os.environ.get('account_sid', None)
    auth_token =  os.environ.get('auth_token', None)
    client = Client(account_sid, auth_token)
    msg = '''
    *FACTURA DE COMPRA*
    *************************************************************************
    *Mensaje*: {Mensaje}
    *Celular*: {Celular}
    *************************************************************************
    '''.format(**factura.dict())
                
    message = client.messages.create(
                            body= msg,
                            from_='whatsapp:+14155238886',#'+14344488907',#
                            to=f'whatsapp:+57{3222441768}'#'+573125599599'
                        )
    return {'respuesta': 'ok', 'status_server':200, 'mensaje': 'ENVIADO'}

# Hacemos un endpoint para recibir los mensajes de whatsapp
@app.post('/mensaje')
async def json_mensaje(factura: MensajeTexto):
    return {f'respuesta': 'ok', 'status_server':200, 'mensaje': {MensajeTexto.Celular}}





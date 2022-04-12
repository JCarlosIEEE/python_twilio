from fastapi import FastAPI

#from fastapi import APIRouter
from pydantic import BaseModel
from twilio.rest import Client
#from fastapi import HTTPException, Request
from os import getenv
#from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse



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

    account_sid ='AC369215d3510e3f069642eff441903bac'
    auth_token = 'dac5b78957d0031fb2b4dd7f8b9dcb00'
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

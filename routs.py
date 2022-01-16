from fastapi import APIRouter
from pydantic import BaseModel
from twilio.rest import Client
from fastapi import HTTPException, Request
from verificar_url import check_url
from os import getenv

router = APIRouter()

class MensajeTexto(BaseModel) :
    Mensaje : str
    Celular : int

# Envio de mensajes a whatsapp
@router.post('/factura')
async def json_factura(cabecera: Request, factura: Factura):
    print(getenv('SECRET'))
    # Comprobamos que el header contiene los datos de autenticación
    if 'Authorization' not in cabecera.headers:
        raise HTTPException(status_code=400, detail={'error': 'No se encontró el header Authorization'})
    # Comprobamos que la llave de autenticación sea correcta
    if cabecera.headers['Authorization'].split(' ')[1] != getenv('SECRET'):
        raise HTTPException(status_code=400, detail={'error': 'La llave de autenticación no es correcta'})

    account_sid ='ACcbdfa04c546c72666d1a632805129e30'
    auth_token = '9968c719ac23c92b76f263b875c57599'
    client = Client(account_sid, auth_token)
    msg = '''
    *FACTURA DE COMPRA*
    *************************************************************************
    *Nombre*: {Nombre_Cliente}
    *Fecha*: {Fecha_Creacion}
    *Ubicacion*: {Ubicacion_Entrega}
    *Dirección*: {Direccion_Entrega}
    *Celular*: {Celular}
    *Estado*: {Estado_Pedido}
    *Estado Pago*: {Estado_Pago}
    *************************************************************************
    '''.format(**factura.dict())
                
    message = client.messages.create(
                            body= msg,
                            from_='whatsapp:+14155238886',#'+14344488907',#
                            to=f'whatsapp:+57{factura.Celular}'#'+573125599599'
                        )
    return {'respuesta': 'ok', 'status_server':200, 'mensaje': 'ENVIADO'}



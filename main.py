from fastapi import FastAPI
from starlette.routing import Router
from routs import router
from dotenv import load_dotenv

app = FastAPI(title= 'Chatbot en whatsapp',
              description= 'Chatbot de prueba con FastApi y Twilio', 
              version= '0.1.0')

app.include_router(router)

load_dotenv()
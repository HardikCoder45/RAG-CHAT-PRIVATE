from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
import json

with open("models.json", 'r') as file:
    data = json.load(file)
models =data['models']
     

class Models:
    def __init__( self):
       pass
     
    def llama(self):
       self.llama = ChatGroq(model=models[0]['model'],api_key=models[0]['api-key'])
       return self.llama
    def mistral(self):
       self.mistral = ChatMistralAI(model=models[1]['model'],api_key=models[1]['api-key'])
       return self.mistral
    def gemma(self):
       self.gemma = ChatGroq(model=models[2]['model'],api_key=models[2]['api-key'])
       return self.gemma
    
    
 

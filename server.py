from fastapi import FastAPI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

from langserve import add_routes

import os

import uvicorn

from dotenv import load_dotenv

load_dotenv()



groq_api_key = os.getenv("GROQ_API_KEY")



model = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")



#Create prompt template 

system_Template = "Translate the following into{language}:"

prompt_template = ChatPromptTemplate.from_messages([('system',system_Template),('user','{text}')])



parser=StrOutputParser()



#create chain 



chain = prompt_template | model | parser



 # APP defination 



app =  FastAPI(

    title="Langchain Server",

    version="1.0",

    description="A simple API server using Langchain's Runnable interfaces",

 )



add_routes(

    app,

    chain,

    path="/chain",

)



if __name__ == "__main__":

uvicorn.run(app, host="localhost",port=8000)








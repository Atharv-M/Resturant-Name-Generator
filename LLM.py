import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# ✅ Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyC9eXzJNZNtUlNoFyyTBHkLww2LMefw_7s"

# Create LLM instance (Gemini 1.5 Pro)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.6)

# Query the model
name = llm.invoke("I want to open a restaurant for Italian food. Suggest a one fancy name for this. Just a single name not more information")
print(name.content)



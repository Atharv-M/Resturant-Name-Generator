import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

os.environ["GOOGLE_API_KEY"] = "AIzaSyC9eXzJNZNtUlNoFyyTBHkLww2LMefw_7s"
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.6)
name = llm.invoke("I want to open a restaurant for Italian food. Suggest a one fancy name for this. Just a single name not more information")


def generate_resturant_name_and_items(cuisine):
    Prompt_Template_Name = PromptTemplate(
        input_varibales=['Cuisine'],  # input varible should be plural
        template=" I want to open a restaurant for {Cuisine} Food. Suggest a one fancy name for this. Just a single name not more info"
    )
    Resturant_name_chain = LLMChain(llm=llm, prompt=Prompt_Template_Name,
                                    output_key="restaurant_name")  # output_key is neccesary for each output

    Prompt_Template_Items = PromptTemplate(
        input_varibales=['restaurant_name'],
        template="Suggest me some menu items for {restaurant_name}. Return it as a comma seprated list. just menu items name not unnessary info"
    )
    Resturant_Menu_item = LLMChain(llm=llm, prompt=Prompt_Template_Items, output_key="menu_items")  # Secound chain

    chain = SequentialChain(chains=[Resturant_name_chain, Resturant_Menu_item],
                            input_variables=['Cuisine'],
                            output_variables=["restaurant_name", "menu_items"]
                            )
    response=chain({"Cuisine": cuisine})
    return response

if __name__=="__main__":
    print(generate_resturant_name_and_items("Italian"))
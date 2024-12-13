from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr
import json

template = """

You are my software developer assistant, you have been given a task to generate database schemas for an App, 
based on the specified prompt.
The allowed datatypes are:
Text
Number 
Email 
Phone 
Checkbox 
Currency 
Date / Datetime 
Picklist 
Multi Picklist 
URL 
Textarea 
Rich Textarea 
Lookup (foreign key to another database table)

You must only give output as the final generated schema (json), don't include any other text in the response. 
The output must always be a database schema or Error message: "Insufficient Details".
App details : {user_input}

"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def schema_generation():
    print("welcome to the AI schema generator. type 'exit' to end")
    while True:
        user_input = input()
        if user_input.lower()=="exit":
            break
        Result = chain.invoke(input=user_input)
        print(type(Result))
def pretty_print_json(parsed_dict):
    return json.dumps(parsed_dict, indent=4)


def display_schema():
    schema_str = pretty_print_json(schema)
    return schema_str 

def process_prompt(prompt):
    Result = chain.invoke(input=prompt)
    json_dict= json.loads(Result)
    json_ = json.dumps(json_dict,indent=4)
    return json_  

interface = gr.Interface(
    fn=process_prompt,              
    inputs=gr.Textbox(label="Enter Prompt"),  
    outputs=gr.Textbox(label="Output JSON"),  
    title="Prompt to JSON",           
    description="Enter a prompt and get the response in JSON format." 
)

interface.launch()


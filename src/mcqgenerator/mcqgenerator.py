import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain

from langchain_core.runnables import RunnableLambda, RunnableSequence  

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

TEMPLATE="""
Text: {text}
You are an expert MCQ maker. Given the above text,it is you job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as guide .\
Ensure to make {number} MCQs


"""

generation_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone"],
    template=TEMPLATE,
)

quiz_chain = generation_prompt | llm

TEMPLATE2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the the quiz. Only use at max 50 words for complexity 
if the quiz is not at per with the congnitive and analytical abilities of the students,\
update the quiz which needs to be changed and change the tone such that it is more suitable for the students.\
Quiz_MCQs:
{quiz}
Check form an expert English Writer of the above quiz:
"""

review_prompt = PromptTemplate(input_variables=["subject","quiz"],
    template=TEMPLATE2,
)

review_chain = review_prompt | llm


file_path = "C:/Users/Ujjwal/Desktop/Projects/mcqgen/data.txt"

with open(file_path, "r") as file:
    TEXT = file.read()




def review_result(payload: dict):
    try:
        text = payload["text"]
        number = payload["number"]
        subject = payload["subject"]
        tone = payload["tone"]

        quiz_output = quiz_chain.invoke({
            "text": text,
            "number": number,
            "subject": subject,
            "tone": tone
        })

        review_output = review_chain.invoke({
            "quiz": quiz_output.content,
            "subject": subject
        })

        return {
            "quiz": quiz_output.content,
            "review": review_output.content
        }
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

# def prepare_review_input(quiz_output, original_input):
#     return {
#         "quiz": quiz_output.content, 
#         "subject": original_input["subject"]
#     }
evaluation_chain = (
   
#     quiz_chain
#     | RunnableLambda(lambda quiz_output, config: {
#        "text":TEXT,
#        "number": NUMBER,
#         "subject": SUBJECT,
#         "tone": TONE,
#         "quiz_output": quiz_chain.invoke

#     })
#     | RunnableLambda(lambda d: prepare_review_input(d["quiz_output"], d["original_input"]))
#     | review_prompt
#     | llm
 )




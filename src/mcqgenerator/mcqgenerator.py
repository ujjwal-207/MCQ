import os
import json
import traceback
import pandas as pd
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

TEMPLATE="""
Text: {text}
You are an expert MCQ maker. Given the above text, create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.

Your response should be in the following JSON format:
{{
    "1": {{
        "mcq": "question here",
        "options": {{
            "a": "choice 1",
            "b": "choice 2",
            "c": "choice 3",
            "d": "choice 4"
        }},
        "correct": "correct_option_letter"
    }}
}}

Ensure to make {number} MCQs and format the response exactly as shown above.
"""

generation_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone"],
    template=TEMPLATE,
)

quiz_chain = generation_prompt | llm | JsonOutputParser()

TEMPLATE2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
Review the quiz and provide analysis in the following JSON format:
{{
    "analysis": "Your 50-word analysis here",
    "complexity_score": "score between 1-10",
    "suggestions": "improvement suggestions if any"
}}

Quiz to review:
{quiz}
"""

review_prompt = PromptTemplate(input_variables=["subject","quiz"],
    template=TEMPLATE2,
)

review_chain = review_prompt | llm |  JsonOutputParser()


file_path = "C:/Users/Ujjwal/Desktop/Projects/mcqgen/data.txt"

with open(file_path, "r") as file:
    TEXT = file.read()




def review_result(payload: dict): #payload is a dictionary containing the text, number of questions, subject, and tone
    try:
        text = payload["text"].strip()#stripe removed leading and trailing spaces like whitespaces
        if not text:
            raise ValueError("Text cannot be empty")
        number = payload["number"]
        subject = payload["subject"]
        tone = payload["tone"]

        quiz_output = quiz_chain.invoke({
            "text": text,
            "number": number,
            "subject": subject,
            "tone": tone
        })
        #  # Convert quiz_output to string if it's a dict
        # quiz_str = json.dumps(quiz_output) if isinstance(quiz_output, dict) else quiz_output

        review_output = review_chain.invoke({
            "quiz": quiz_output,
            "subject": subject
        })

        return {
            "quiz": quiz_output,
            "review": review_output,
        }
    except Exception as e:
        logging.error("Error in review_result: %s", str(e))
        traceback.print_exc()
        return {"error": str(e)}





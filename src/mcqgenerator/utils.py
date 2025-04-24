import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)  # create a pdf reader object || PdfReader is used to read the pdf file to access the properties of the pdf file 
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text() # extract text from each page of the pdf file and store it in the text variable 
            return text
            
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):  # check if the file is a text file
        return file.read().decode("utf-8") # read the content of the text file and decode it to utf-8 format || decode is used to convert the bytes to string format
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )

def get_table_data(quiz_str): # quiz_str is a string that contains the quiz data in JSON format || recieved from the response of the review_result function
    try:
        # convert the quiz from a str to dict
        quiz_dict = quiz_str if isinstance(quiz_str, dict) else json.loads(quiz_str) # convert the quiz string to a dictionary format || loads is used to parse the JSON string and convert it into a Python dictionary

        quiz_table_data=[]
        
        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items(): #
            mcq=value["mcq"]
            options=" || ".join(  # join the options with " || " separator
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items() # iterate over the options dictionary and extract the option and its value
                 
                 ]
            )
            
            correct=value["correct"] # extract the correct answer from the dictionary
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct}) # append the extracted data to the quiz_table_data list in a dictionary format
        
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__) # print the stack trace of the exception
        return False


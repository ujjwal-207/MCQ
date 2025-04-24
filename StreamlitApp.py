import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from src.mcqgenerator.mcqgenerator import review_result
from src.mcqgenerator.logger import logging

#loading json file

with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#creating a title for the app
st.title("MCQs Creator Application with LangChain 🦜⛓️")

#Create a form using st.form
with st.form("user_inputs"):
    #File Upload
    uploaded_file=st.file_uploader("Uplaod a PDF or txt file")

    #Input Fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

    #Subject
    subject=st.text_input("Insert Subject",max_chars=20)

    # Quiz Tone
    tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    #Add Button
    button=st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                logging.info("File read successfully:{uploaded_file.name}") 
                
                
                response=review_result(
                    {
                    "text": text,
                    "number": mcq_count,
                    "subject":subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                    }
                )
                logging.info("Response received successfully")
                #st.write(response)
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__) #type is used to get the type of the exception and e is used to get the exception object and __traceback__ is used to get the traceback object
                st.error("Error occurred while processing the file.")

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__) #traceback is used to print the stack trace of the exception
                st.error("Error")

            else:
                if isinstance(response, dict):
                    #Extract the quiz data from the response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz) #get_table_date is a function that takes the quiz data and returns the table data in a list of dictionaries format || it passes the quiz data from the response to the get_table_data function to extract the quiz data from the response
                        if table_data is not None: ##check if the table data is not None like empty
                            df=pd.DataFrame(table_data) #convert the table data to a pandas dataframe || DataFrame is a 2-dimensional labeled data structure with columns of potentially different types
                            df.index=df.index+1 #start the index from 1 instead of 0 because the index starts from 0 by default in pandas
                            st.table(df) #display the table data in a table format using st.table function || st.table is used to display the dataframe in a table format
                            #Display the review in atext box as well
                            st.text_area(label="Review", value=response["review"]) #display the review in a text area format using st.text_area function || st.text_area is used to display the review in a text area format
                        else:
                            st.error("Error in the table data")# #display the error message if the table data is None like empty

                else:
                    st.write(response)



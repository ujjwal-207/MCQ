from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="ujjwal nepal",
    author_email="ujjwalnepal715@gmail.com",
    install_requires=["genai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
    )
# MCQ Generator

A streamlined application that automatically generates Multiple Choice Questions (MCQs) from uploaded PDF or text documents using LangChain and LLM technology.

## Features

- **Document Processing**: Upload and process PDF or text files
- **Custom MCQ Generation**: Create questions based on specific topics from the uploaded content
- **Difficulty Selection**: Choose between Easy, Medium, and Hard difficulty levels
- **User-Friendly Interface**: Simple and intuitive Streamlit-based UI

## How It Works

The application uses a pipeline approach to generate high-quality MCQs:

1. **Document Loading**: The system accepts PDF or text files as input
2. **Text Processing**: Content is extracted and processed for knowledge extraction
3. **LLM Integration**: Utilizes LangChain framework to connect with Large Language Models
4. **Question Generation**: Creates contextually relevant MCQs based on user-specified parameters
5. **Result Display**: Presents formatted questions with multiple choice options

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ujjwal-207/MCQ.git
   cd MCQ
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Upload a PDF or text file using the file uploader
2. Enter the specific topic you want MCQs for
3. Select the difficulty level (Easy, Medium, Hard)
4. Click "Generate MCQs"
5. View and use the generated questions

## Technology Stack

- **Streamlit**: Frontend interface
- **LangChain**: Framework for LLM operations
- **PyPDF2/PDFPlumber**: PDF processing
- **OpenAI API**: Question generation engine

## Project Structure

```
MCQ/
├── app.py                  # Main Streamlit application
├── mcq_generator.py        # Core MCQ generation logic
├── document_processor.py   # Document loading and text extraction
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (API keys)
└── README.md               # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the LLM technology
- LangChain for the framework that makes LLM integration easier
- Streamlit for the simple yet powerful UI framework
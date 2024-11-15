# LLMSmartChat
This project leverages a Large Language Model (LLM) (OpenAI) to answer user queries based on the contents of a pdf file. By utilizing efficient document chunking and retrieval techniques, this system ensures that only the most relevant sections of the document are used to generate accurate and context-specific answers.

## Features
- Document Parsing and Indexing: Uses PDF parsing libraries (e.g., pdfplumber) to extract and preprocess text from PDF files.
- Efficient Retrieval: Automatically chunks and indexes document contents for quick and accurate retrieval of relevant sections.
- OpenAI API Integration: Leverages OpenAI’s GPT-4 model for natural language generation, enabling context-aware responses to user queries.
- Confidence-Based Filtering: Implements a mechanism to detect and respond to low-confidence answers, improving reliability.
- Expandable: Designed to support additional document types or retrieval systems (e.g., adding LlamaIndex or LangChain).

## Setup and Installation
### Prerequisites
  - Python 3.12
  - OpenAI API Key: You’ll need an OpenAI account and API key to access GPT-4.

### Installation
  1. Clone the repository:
     ```
      git clone git@github.com:nisthaKumar/LLMSmartChat.git
      cd LLMSmartChat
     ```
  3. Create a virtual environment:
     ```
      python3 -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
  5. Install dependencies:
     ```
     pip install -r requirements.txt

     ```
  6. Set up OpenAI API Key:

      - Export the OpenAI API key as an environment variable:

        ```
        export OPENAI_API_KEY="your_openai_api_key"
        ```
      - Alternatively, create a .env file in the project root and add:

        ```
        OPENAI_API_KEY=your_openai_api_key
        ```
## Project Structure
```
LLMSmartChat
├── docs
    ├── handbook.pdf            # PDF file to be passed as argument
├── src/
    ├── pdf_processor.py        # PDF text extraction and chunking logic
    ├── text_embedding.py       # Embedding generation using SentenceTransformer
    ├── retriever.py            # Retrieve relevant text chunks using FAISS
    ├── response_generator.py   # Generate answers using OpenAI GPT
    ├── main.py                 # Main script to run the system
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
```
## Usage
### Running the System
You can run the LLMSmartChat using the command below, which will process a PDF and answer a list of questions based on its contents:
```
python src/main.py <pdf_path> <question_1> <question_2> ...
```
- <pdf_path>: The path to the PDF document you want to process.(docs/handbook.pdf in our case)
- <question_1>, <question_2>, etc.: A list of questions to ask the system based on the PDF

### Example
```
python src/main.py docs/handbook.pdf "What is the name of the company?" "Who is the CEO of the company?" "How many employees are there in this company?"
```

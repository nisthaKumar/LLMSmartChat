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
  4. Install dependencies:
     ```
     pip install -r requirements.txt

     ```
  5. Set up OpenAI API Key:

      - Export your OpenAI API key as an environment variable:

        ```
        export OPENAI_API_KEY="your_openai_api_key"
        ```
      - Alternatively, create a .env file in the project root and add:

        ```
        OPENAI_API_KEY=your_openai_api_key
        ```

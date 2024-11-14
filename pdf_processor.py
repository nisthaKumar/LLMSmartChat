import pdfplumber

def read_and_process_pdf(pdf_path, chunk_size=200):
    text_chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + " "
    
    # Split text into chunks of `chunk_size` words
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        text_chunks.append(chunk)
    
    return text_chunks

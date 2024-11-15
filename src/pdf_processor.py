import pdfplumber
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_process_pdf(pdf_path, chunk_size=200):
    text_chunks = []
    logging.info(f"Opening PDF file: {pdf_path}")

    try:
        with pdfplumber.open(pdf_path) as pdf:
            logging.info(f"PDF opened successfully. Total pages: {len(pdf.pages)}")

            text = ""
            for page_num, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                text += page_text + " "
                
            logging.info(f"Extraction completed")
        # Split text into chunks of `chunk_size` words
        words = text.split()
        logging.info(f"Total words extracted from PDF: {len(words)}")

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            text_chunks.append(chunk)
            logging.debug(f"Created chunk {len(text_chunks)} with {len(chunk.split())} words.")

        logging.info(f"Total chunks created: {len(text_chunks)}")

    except Exception as e:
        logging.error(f"Error occurred while processing PDF: {e}")
        raise

    return text_chunks

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
    def process_pdf(self, pdf_path):
        """Load and process a PDF file into chunks."""
        try:
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            
            # Split into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap
            )
            chunks = text_splitter.split_documents(documents)
            
            print(f"Processed PDF: {pdf_path}")
            print(f"Total chunks: {len(chunks)}")
            
            return chunks
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return []

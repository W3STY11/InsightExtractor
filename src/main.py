from src.document_processor import DocumentProcessor
from src.knowledge_extractor import KnowledgeExtractor
from src.prompt_generator import PromptGenerator
import os
import google.generativeai as genai

def load_api_key():
    """Load API key from .api_key file or prompt user for it."""
    # Check if we have a saved API key
    if os.path.exists(".api_key"):
        with open(".api_key", "r") as f:
            api_key = f.read().strip()
            # Verify the key is not empty
            if api_key:
                return api_key
    
    # If no saved key or it's empty, prompt the user
    api_key = input("Enter your Google API key for Gemini: ")
    
    # Save the key for future use
    with open(".api_key", "w") as f:
        f.write(api_key)
    
    return api_key

def main():
    # Get API key
    api_key = load_api_key()
    
    # Initialize components
    print("Initializing document processor...")
    doc_processor = DocumentProcessor()
    
    print("Initializing knowledge extractor...")
    knowledge_extractor = KnowledgeExtractor(api_key=api_key)
    
    print("Initializing prompt generator...")
    prompt_generator = PromptGenerator()
    
    # Process papers
    while True:
        print("\n=== Prompt Engineering Assistant ===")
        print("1. Process a new research paper")
        print("2. Generate an optimized prompt")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == "1":
            pdf_path = input("Enter path to research paper PDF: ")
            if os.path.exists(pdf_path):
                print(f"Processing {pdf_path}...")
                chunks = doc_processor.process_pdf(pdf_path)
                if chunks:
                    print("Extracting insights...")
                    insights = knowledge_extractor.extract_insights(chunks)
                    print("Creating knowledge base...")
                    knowledge_extractor.create_knowledge_base(chunks, insights)
                    print("Paper processed successfully!")
                else:
                    print("Failed to process paper.")
            else:
                print(f"File not found: {pdf_path}")
                
        elif choice == "2":
            user_goal = input("What is your goal for this prompt? ")
            context = input("Describe the context or use case: ")
            print("\nGenerating optimized prompt based on research insights...")
            
            # Load existing knowledge base if it exists
            try:
                from langchain_community.vectorstores import Chroma
                from langchain_community.embeddings import HuggingFaceEmbeddings
                
                embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
                vectorstore = Chroma(persist_directory="./knowledge_db", embedding_function=embeddings)
                
                result = prompt_generator.generate_optimized_prompt(vectorstore, user_goal, context)
                print("\n" + result)
            except Exception as e:
                print(f"Error generating prompt: {e}")
                print("Make sure you've processed at least one paper first.")
                
        elif choice == "3":
            print("Exiting...")
            break
            
        else:
            print("Invalid option. Please select 1-3.")

if __name__ == "__main__":
    main()

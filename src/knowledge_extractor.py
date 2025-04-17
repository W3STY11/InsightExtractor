from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import google.generativeai as genai

class KnowledgeExtractor:
    def __init__(self, api_key=None, temperature=0.1):
        # Set Google API key from environment variable or parameter
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
            genai.configure(api_key=api_key)
        elif "GOOGLE_API_KEY" in os.environ:
            genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        else:
            raise ValueError("No Google API key provided. Please provide a valid API key.")
        
        # Verify API key is working
        try:
            model = genai.GenerativeModel('gemini-1.5-pro')
            model.generate_content("API key test")
            print("Google Gemini API key verified.")
        except Exception as e:
            raise ValueError(f"Invalid Google API key: {e}")
        
        # Initialize extraction prompt
        self.extraction_prompt = PromptTemplate(
            input_variables=["chunk"],
            template="""
            You are an expert in prompt engineering research.
            Extract the key insights, methodologies, and findings from this research paper excerpt:
            
            {chunk}
            
            Provide the following:
            1. Main concepts discussed
            2. Methodologies or techniques presented
            3. Key findings or results
            4. Potential applications
            """
        )
        
        # Initialize Gemini model
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=temperature)
        self.extraction_chain = LLMChain(llm=self.llm, prompt=self.extraction_prompt)
        
    def extract_insights(self, chunks):
        """Extract insights from document chunks."""
        all_insights = []
        
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i+1}/{len(chunks)}...")
            try:
                result = self.extraction_chain.run(chunk=chunk.page_content)
                all_insights.append(result)
            except Exception as e:
                print(f"Error processing chunk {i+1}: {e}")
                all_insights.append("Error extracting insights from this chunk.")
            
        print(f"Extracted insights from {len(chunks)} chunks")
        return all_insights
    
    def create_knowledge_base(self, chunks, insights, persist_directory="./knowledge_db"):
        """Store processed insights in a vector database."""
        # Initialize embeddings
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Combine chunks with their extracted insights
        enhanced_docs = []
        for i, chunk in enumerate(chunks):
            if i < len(insights):
                # Add insights to metadata
                chunk.metadata["insights"] = insights[i]
                enhanced_docs.append(chunk)
        
        # Create vector store
        vectorstore = Chroma.from_documents(
            documents=enhanced_docs,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        
        print(f"Created knowledge base with {len(enhanced_docs)} documents")
        print(f"Knowledge base persisted to: {persist_directory}")
        
        return vectorstore

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class PromptGenerator:
    def __init__(self, temperature=0.7):
        # Initialize prompt generation template
        self.prompt_gen_template = PromptTemplate(
            input_variables=["goal", "context", "relevant_insights"],
            template="""
            Based on the following research insights about prompt engineering and the specific goal,
            generate an optimized prompt:
            
            GOAL: {goal}
            CONTEXT: {context}
            RELEVANT RESEARCH INSIGHTS:
            {relevant_insights}
            
            Create a well-structured prompt that incorporates these research findings and is optimized for the stated goal.
            
            Format your response as:
            PROMPT TEMPLATE:
            [The generated prompt with placeholders for variables if needed]
            
            EXPLANATION:
            [Explain how this prompt incorporates the research insights and why it should be effective]
            """
        )
        
        # Initialize Gemini with higher temperature for creativity
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=temperature)
        self.prompt_chain = LLMChain(llm=self.llm, prompt=self.prompt_gen_template)
    
    def generate_optimized_prompt(self, vectorstore, user_goal, context, k=3):
        """Generate optimized prompts based on user requirements."""
        # Retrieve relevant insights
        query = f"{user_goal} {context}"
        results = vectorstore.similarity_search(query=query, k=k)
        
        # Extract insights from retrieved documents
        relevant_insights = "\n".join([doc.metadata.get("insights", "") for doc in results])
        
        # Generate prompt
        result = self.prompt_chain.run(
            goal=user_goal,
            context=context,
            relevant_insights=relevant_insights
        )
        
        return result

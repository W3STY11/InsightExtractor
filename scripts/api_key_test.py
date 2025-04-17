import google.generativeai as genai
import os

def test_api_key():
    # Try to load from file first
    if os.path.exists(".api_key"):
        with open(".api_key", "r") as f:
            api_key = f.read().strip()
    else:
        # Or get from user input
        api_key = input("Enter your Google Gemini API key: ")
    
    # Configure the API
    genai.configure(api_key=api_key)
    
    try:
        # Test with a simple prompt
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content("Hello, can you confirm this API key is working?")
        
        print("\n=== API KEY TEST SUCCESSFUL ===")
        print("Response from Gemini:")
        print(response.text)
        print("\nAPI key is valid and working correctly.")
        
        return True
    except Exception as e:
        print("\n=== API KEY TEST FAILED ===")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_api_key()

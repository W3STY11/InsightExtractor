# InsightExtractor

## Research-Powered Prompt Engineering Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**InsightExtractor** is an advanced system that extracts insights from research papers on prompt engineering, LLMs, and AI to generate optimized prompts based on cutting-edge academic findings. It processes academic PDFs, extracts key methodologies and findings, and uses this knowledge to craft research-backed prompts for specific use cases.

---

## 🌟 Features

- **Research Paper Processing**: Extract text from PDF research papers and split into optimal chunks  
- **AI-Powered Insight Extraction**: Analyze research papers to extract key concepts, methodologies, and findings  
- **Knowledge Base Creation**: Build a searchable vector database of research insights  
- **Optimized Prompt Generation**: Generate tailored prompts based on research findings for any specific goal  
- **Extensible Architecture**: Easily add new papers to expand the knowledge base over time  

---

## 📋 Requirements

- Python 3.8+  
- Google Gemini API key (or OpenAI API key with minor modifications)  
- PDF research papers (not included in the repository)  

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/W3STY11/InsightExtractor.git
cd InsightExtractor

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p data/papers knowledge_db
```

---

## 🔑 API Key Setup

Before running the system, you need to set up your Google Gemini API key:

```bash
# Option 1: Create a .api_key file
echo "YOUR_GEMINI_API_KEY" > .api_key
```

Or set it as an environment variable:

```powershell
# For Windows (PowerShell)
$env:GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
```

```bash
# For macOS/Linux
export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

---

## 📖 Usage

### Starting the Application

```bash
python -m src.main
```

### Processing Research Papers

1. Select option `1` from the main menu  
2. Enter the full path to a research paper PDF  
3. Wait for the system to process the paper and extract insights  
4. The paper will be added to your knowledge base  

### Generating Optimized Prompts

1. Select option `2` from the main menu  
2. Enter your prompt goal (e.g., "Generate a creative story")  
3. Provide context about your use case (e.g., "For middle school students")  
4. The system will generate a research-backed prompt optimized for your goal  

---

## 📁 Repository Structure

```
InsightExtractor/
├── data/
│   └── papers/             # Directory for storing research papers
├── knowledge_db/           # Vector database storage for extracted insights
├── src/
│   ├── __init__.py
│   ├── document_processor.py  # PDF loading and chunking
│   ├── knowledge_extractor.py # Research insight extraction
│   ├── prompt_generator.py    # Optimized prompt generation
│   └── main.py                # Main application
├── scripts/
│   └── api_key_test.py        # Script to test API key
├── requirements.txt           # Project dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # This README file
```

---

## 🧠 How It Works

InsightExtractor follows a four-stage process:

1. **Document Processing**: PDFs are converted to text and split into manageable chunks with appropriate overlap to maintain context  
2. **Insight Extraction**: Each chunk is analyzed using the Gemini API to extract key concepts, methodologies, findings, and applications from the research papers  
3. **Knowledge Base Creation**: Extracted insights are stored in a vector database (Chroma) using embeddings that capture the semantic meaning of the content  
4. **Prompt Generation**: When given a prompt goal and context, the system searches the knowledge base for relevant research insights and uses them to generate an optimized, research-backed prompt  

---

## 📊 Performance

The system has been tested with a variety of research papers and consistently produces high-quality, research-informed prompts.  
Processing time varies based on document length:

| Document Size | Processing Time | Chunks | Storage Size |
|---------------|------------------|--------|---------------|
| 10 pages      | ~5-10 minutes    | ~30    | ~5 MB         |
| 25 pages      | ~15-25 minutes   | ~75    | ~12 MB        |
| 50+ pages     | ~30-60 minutes   | 150+   | ~25+ MB       |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

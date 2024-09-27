# Negotiation ChatBot

## Features

### Negotiation Capabilities
- Responds intelligently to user price offers.
- Maintains a polite tone while explaining pricing constraints.

### Sentiment Analysis
- Assesses the politeness of user input.
- Tailors responses based on the user's emotional tone.

### Interactive User Interface
- Built using Streamlit for a clean and intuitive user experience.

## Technologies Used
- **Python**: Programming language for development.
- **Streamlit**: Web framework for building interactive applications.
- **Google Gemini LLM**: Generative model for dynamic response formulation.
- **NLTK**: Natural Language Toolkit for processing text, specifically for sentiment analysis.
- **Regex**: For extracting numerical values from user input.

## Development Process

### Environment Setup
- Installed necessary packages for Streamlit, Google Gemini, NLTK, and dotenv.
- Set up an environment variable file (.env) to store the API key for Google Gemini.

### Library Imports
- Imported required libraries including Streamlit, Google Gemini, NLTK, and others.

### Configuration
- Initialized NLTK’s sentiment analysis model (VADER).
- Loaded the Google Gemini API key from environment variables.

### Model Initialization
- Initialized the Google Gemini generative model to start a chat session.

### Helper Functions
- Defined functions to handle:
  - Sending messages to the generative model and resolving responses.
  - Analyzing sentiment to determine user politeness.
  - Extracting numerical values from user input using regex.

### User Interface Creation
- Developed the user interface using Streamlit components, including:
  - Text input for user offers.
  - Submission button for initiating negotiations.
  - Chat history display for showing conversation between user and bot.

### User Input Handling
- Processed user input to extract offered prices.
- Determined appropriate responses based on minimum and maximum price thresholds and user sentiment.

### Response Generation
- Called the generative model to obtain responses based on crafted prompts related to user offers.

### Displaying Chat History
- Showed the interaction history between the user and the bot within the Streamlit application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Niket420/NegotiableChatBot.git

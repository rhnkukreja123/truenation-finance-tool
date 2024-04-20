# True Nation PoC

## Description

True Nation PoC is a proof of concept for a sophisticated financial query tool that enables users to input diverse financial queries, ranging from exchange rates between countries to detailed company financials. Leveraging an agent framework, this tool dynamically selects the appropriate function to fetch accurate responses, simulating human-like reasoning and decision-making capabilities.

## Installation

### Prerequisites

Before installing, ensure you have the following API keys which are necessary for the full functionality of the project:
- Alpha Vantage API Key
- OpenAI API Key

These keys should be set as environment variables to secure your credentials and streamline the application's configuration.

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rhnkukreja123/trunation-finance-tool.git
2. **Navigate to the repository directory:**
   ```bash
   cd main_app
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
4. **Set up environment variables:**
   ```bash
    export ALPHA_VANTAGE_API_KEY='your_alpha_vantage_key'
    export OPENAI_API_KEY='your_openai_key'
## Usage

To use the True Nation PoC, follow these steps:

1. **Navigate to the driver script:**
    ```bash
    cd path/to/driver.py
2. **Edit the driver.py to include your query:**
    + Open driver.py in a text editor.
    + Modify the query variable to reflect your specific financial question.
3. **Run the script:**
    ```bash
    python driver.py
This will execute your query and display the fetched results in the console.

## Features
+ Agent Framework: Utilizes an advanced agent framework from OpenAI's Langchain to process and reason about the input queries, ensuring the selection of optimal functions for accurate results.
+ Multi-API Integration: Incorporates multiple APIs including Alpha Vantage for financial data and Pinecone for querying pre-loaded legal documents, enhancing the tool's utility and performance.


## API Reference

To use the APIs integrated in this project, set up your API keys as described in the Installation section. These keys allow the application to authenticate and retrieve data necessary for responding to queries.



## Acknowledgments
Alpha Vantage, OpenAI, and Pinecone for their powerful APIs.

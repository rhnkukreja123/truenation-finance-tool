import requests
import re

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

def get_response_from_openai(openai_prompt):
    api_key="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"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Or whichever model you're using, e.g., "gpt-3.5-turbo"
        "messages": [
                {"role": "system", "content": "You are a helpful assistant designed to answer the user question strictly from the context given alongside."},
                {"role": "user", "content": openai_prompt}
            ],
        "temperature": 0.7,  # Adjust for creativity. Closer to 1.0 makes the responses more creative.
        "max_tokens": 1000,  # Adjust based on how long you expect the response to be
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        response_data=response_data["choices"][0]["message"]["content"]
        return response_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)



def query_parser(query):
    query_parser_prompt=f"Given the Query: {query}, i want you to extract the stock symbol and return just that , and nothing else, no supporting text , just the stock symbol, for example: if it is apple , the symbol should be AAPL, make sure to only give out the symbol and no other text. If only the company name is given, just give out the symbol in that case as well."
    response=get_response_from_openai(query_parser_prompt)

    return response


def query_parser_for_two_currencies(query):
    query_parser_prompt=f"""Given the Query: {query}, i want you to give me the currency symbols for the currencies mentioned in the query, 
                            give the currencies only as the output and nothing else.
                            For example:
                            Query: What is the exchange rate between the british currency and the indian currency?
                            Output: INR , GBP"""
    
    response=get_response_from_openai(query_parser_prompt)

    pattern = re.compile(r"(?<=\-\s)[A-Z]{3}|[A-Z]{3}")
    matches = pattern.findall(response)


    if len(matches) >= 2:
        return matches[0], matches[1]
    else:
        return None, None


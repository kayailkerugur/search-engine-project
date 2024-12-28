import os
import requests
import openai

def search_gpt(query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Search results for: {query}",
        max_tokens=100
    )
    return response["choices"][0]["text"]

def search_google(query):
    api_key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CX")
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx
    }
    response = requests.get(url, params=params)
    return response.json()

def search_bing(query):
    api_key = os.getenv("BING_API_KEY")
    url = f"https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query}
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def search_gpt(query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Search results for: {query}",
        max_tokens=100
    )
    return response["choices"][0]["text"]

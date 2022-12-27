import openai
import config

def generate_joke(prompt):
    """
    Uses the OpenAI ChatGPT API to generate a joke based on the specified prompt.
    Returns the generated joke as a string.
    """
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=0.5)
    return response["choices"][0]["text"]
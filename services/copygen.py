import openai
from utils.prompts import PROMPT_TEMPLATES
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_copy(data):
    template_name = data.get("template")
    variables = data.get("variables", {})

    prompt_template = PROMPT_TEMPLATES.get(template_name)
    if not prompt_template:
        return {"error": "Invalid template selected."}

    try:
        prompt = prompt_template.format(**variables)
    except KeyError as e:
        return {"error": f"Missing variable: {str(e)}"}

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a world-class copywriter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return {"copy": response.choices[0].message.content.strip()}

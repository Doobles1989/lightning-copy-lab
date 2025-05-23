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

    try:
        print("Prompt to OpenAI:", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ✅ Fully available to all OpenAI users
            messages=[
                {"role": "system", "content": "You're a world-class copywriter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return {"copy": response.choices[0].message.content.strip()}
    except Exception as e:
        print("OpenAI error:", e)
        return {"error": str(e)}

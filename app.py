import openai
from flask import Flask, request, jsonify, render_template_string

openai.api_key = "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"

app = Flask(__name__)

HTML_TEMPLATE = """..."""  # Use the long HTML_TEMPLATE from earlier

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/generate-ad", methods=["POST"])
def generate_ad():
    data = request.get_json()
    niche = data["niche"]
    goal = data["goal"]
    adtype = data["adtype"]

    prompt = f"Generate a Facebook ad for a {niche} business. The goal is to {goal.lower()}. Include a headline, body text, and a call-to-action."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.choices[0].message.content.strip().split("\n")
    headline = text[0].replace("Headline:", "").strip()
    body = text[1].replace("Body:", "").strip()
    cta = text[2].replace("CTA:", "").strip()

    return jsonify({
        "copy": {
            "headline": headline,
            "body": body,
            "cta": cta
        },
        "settings": {
            "objective": goal,
            "budget": "$20/day",
            "targeting": f"People interested in {niche}, ages 25–55",
            "placement": "Facebook & Instagram Feed"
        }
    })

app.run(host="0.0.0.0", port=7860)

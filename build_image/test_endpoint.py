import torch
from transformers import pipeline
from fastapi import FastAPI

# Load the pipeline for the TinyLlama model
pipe = pipeline("text-generation", 
                model="TinyLlama/TinyLlama-1.1B-Chat-v0.6",
                torch_dtype=torch.bfloat16, 
                device_map="auto")


# Create the FastAPI app
app = FastAPI()

# Define the root endpoint (just for info)
@app.get("/")
def read_root():
    return {"API": "Phi endpoint"}

# Define the generate endpoint
@app.get("/generate/")
def generate(text: str):
    # Format the input text
    messages = [
        {
            "role": "system",
            "content": "You are a friendly chatbot.",
        },
        {"role": "user", "content": text},
    ]
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    # Generate the response
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    return {"response": outputs[0]["generated_text"]}


# curl -X 'GET' \
#  'http://35.188.185.170/generate/?text=Tell%20a%20joke' \
#  -H 'accept: application/json'
from fastapi import FastAPI, Query
import ollama

app = FastAPI()

@app.get("/sentence")
def sentence(word: str = Query(..., description="Word to create the sentence")):
  message = f"Generate a sentence with the word '{word}'."
  options = ollama.Options(
    num_ctx=2048,
    temperature=0.5,
    top_k=50,
    top_p=1,
    presence_penalty=0.5,
    frequency_penalty=0.5,
    stop=["<|user|>", "<|assistant|>"]
  )
  response = ollama.chat(
    model="tinyllama",
    messages=[
      {
        "role":"user",
        "content":message
      } 
    ],
    options=options
  )
  return {"[✓] resposta": response.get("message", {}).get("content", '')}



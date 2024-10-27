from fastapi import FastAPI, Query
import ollama

app = FastAPI()

@app.get("/sentence")
def sentence(word: str = Query(..., description="Word to create the sentence")):
  message = f"Make a small sentence with the word '{word}' in it."
  response = ollama.chat(model="tinyllama", messages=[
    {
      "role":"user",
      "content":message
    }
  ])
  return {"[✓] resposta": response.get("message", {}).get("content", '')}



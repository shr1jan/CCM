from fastapi import FastAPI, Request
from app.verify import verify_output
from app.config import load_corpus

app = FastAPI()
corpus_index = load_corpus()

@app.post("/verify")
async def verify(request: Request):
    data = await request.json()
    ai_output = data["text"]
    verified = verify_output(ai_output, corpus_index=corpus_index)
    return {"cleaned": verified}

from fastapi import FastAPI
import tacotron

app = FastAPI()

@app.get('/speak')
async def speak():
    sample_text = 'سلام بر تو ای جوان آریایی.'
    sample_filename = 'javan'
    tacotron.generate(sample_text, sample_filename)
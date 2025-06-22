from fastapi import FastAPI, Request, Form
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi.responses import Response
import sys
import os

sys.path.append(os.path.abspath("src"))
from Briefly.pipeline.prediction import Predictionpipeline

app = FastAPI(
    title="Briefly - AI Text Summarizer",
    description="Transform long texts into concise summaries with AI",
    version="1.0.0",
    docs_url="/api-docs"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api-docs", tags=["documentation"])
async def api_docs():
    return RedirectResponse(url='/api-docs')

@app.get("/train", tags=["training"])
async def training():
    try:
        os.system("python main.py")
        return {"status": "success", "message": "Training completed successfully! 🚀"}
    except Exception as e:
        return {"status": "error", "message": f"Training failed: {str(e)}"}

@app.post("/predict", tags=["prediction"])
async def predict_route(text: str = Form(...)):
    try:
        obj = Predictionpipeline()
        summary = obj.predict(text)
        return {
            "status": "success",
            "original_text": text,
            "summary": summary,
            "original_length": len(text),
            "summary_length": len(summary),
            "compression_ratio": round((1 - len(summary) / len(text)) * 100, 2)
        }
    except Exception as e:
        return {"status": "error", "message": f"Prediction failed: {str(e)}"}

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy", "service": "Briefly AI Summarizer"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

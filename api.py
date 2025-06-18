from fastapi import FastAPI
from main import run_pipeline

app = FastAPI()

@app.post("/run-pipeline")
def run_pipeline_endpoint():
    run_pipeline()
    return {"message": "Pipeline executed successfully"}

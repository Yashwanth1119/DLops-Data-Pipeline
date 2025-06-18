# DLOps Data Pipeline (Streamlit + MongoDB + Faker)

This project demonstrates an end-to-end **Data Engineering pipeline** with:

- Fake data generation (`Faker`)
- ETL pipeline (`pandas`)
- MongoDB storage
- Streamlit UI to run everything

---

## 📁 Structure

- `generate_data.py`: creates 100K fake records
- `main.py`: runs ETL and loads MongoDB
- `app.py`: Streamlit UI
- `pipeline/`: modular ETL scripts

---

## ⚙️ Setup Instructions

1. Clone the repo and `cd` into it
2. Install dependencies:

```bash
pip install -r requirements.txt
```
## Start MongoDB (local or Docker):
```bash
docker run -d -p 27017:27017 --name mongo mongo
```
## Run the Streamlit App:
```bash
streamlit run app.py
```
## Output
* data/raw_data.csv — Raw fake dataset
* output/cleaned_data.csv — Final CSV
* MongoDB — dlopsdb.cleaned_data collection

## Folder Structure
```bash
dlops-data-pipeline/
├── data/
│   └── raw_data.csv
├── output/
│   └── cleaned_data.csv
├── pipeline/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   └── mongo_loader.py  ← new
├── main.py
├── app.py               ← Streamlit UI
├── requirements.txt
```

##  📈Extensions (Next Steps)
* Add FastAPI interface
* Add MLflow for tracking
* Add Prefect or Airflow orchestration
* Visualize MongoDB data in Streamlit

## yaml

---

## ✅ Final Output Example

After clicking "📦 Generate & Process Data":

- You’ll see 100K records processed
- Output:  
  ✅ Cleaned CSV at `output/cleaned_data.csv`  
  ✅ MongoDB loaded: `dlopsdb.cleaned_data`  
  ✅ Streamlit preview of 1,000 records

---

Would you like:
- A GitHub repo version of this?
- Dockerfile to containerize the whole project?
- Add MongoDB → Streamlit viewer?



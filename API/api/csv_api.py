from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.csv_service import parse_csv
from services.csv_to_xml_convertor import row_to_xml
from config_loader import load_config
import os

router = APIRouter()
config=load_config()

OUTPUT_DIR = config["Csv_to_xml_output_path"]


@router.post("/csv-to-xml")
async def csv_to_xml(
    file: UploadFile = File(None),
    csv_data: str = Form(None)
):

    # STEP 1: Get CSV content
    if file:
        content = (await file.read()).decode("utf-8")

    elif csv_data:
        content = csv_data

    else:
        raise HTTPException(
            status_code=400,
            detail="Provide either file or csv_data"
        )

    # STEP 2: Parse CSV → rows
    rows = parse_csv(content)

    if not rows:
        raise HTTPException(
            status_code=400,
            detail="No data found in CSV"
        )
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_files = []

    # STEP 3: Convert each row → XML
    results = []

    for row in rows:
        xml = row_to_xml(row)
        results.append(xml)

    return {
        "total_records": len(results),
        "xml_records": results
    }
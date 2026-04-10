from fastapi import FastAPI,HTTPException
from fastapi.responses import Response
from validator import validate_json
from converter import convert_json_to_xml
from dicttoxml import dicttoxml

app = FastAPI()

@app.post("/json-to-xml")
async def json_to_xml(data: dict):
    
    is_valid, message = validate_json(data) 
    if not is_valid:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {message}")
    #Convert JSON to XML
    xml_data = convert_json_to_xml(data)

    return Response(content=xml_data, media_type="application/xml")





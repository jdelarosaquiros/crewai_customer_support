import warnings
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from src.crewai_customer_support.crew import CrewaiCustomerSupport

# A constant or environment-based API key for demonstration:
API_KEY = "crewai-dZlh2oodfEtyFq904NQd04zUQxe2osOys7W0dOlmXbiFK1LVuNnStGOwe6r9zJ9EcwJsIW7ZIifLXW4SvaVeaRreH0XfdR4Acbkmrfo21w3A1fUQMBydkWmxc"

# We'll define the header name we expect for the API key
API_KEY_HEADER = "API-Key"
api_key_header = APIKeyHeader(name=API_KEY_HEADER, auto_error=True)

app = FastAPI()

class KickoffInput(BaseModel):
    title: str
    user_content: str

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Validates the API key provided in the request header.
    """
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid or missing API key"
        )
    return api_key

@app.post("/kickoff")
def kickoff(
    input_data: KickoffInput,
    api_key: str = Depends(get_api_key)  # Dependency to enforce API key checking
):
    """
    Kick off the CrewAI Customer Support process using the provided title and user content,
    allowing only requests that supply a valid API key.
    """
    try:
        inputs = {
            "title": input_data.title,
            "user_content": input_data.user_content
        }

        # Run the Crew
        result = CrewaiCustomerSupport().crew().kickoff(inputs=inputs)

        # For demonstration purposes
        print(f"Running CrewaiCustomerSupport with: {inputs}")

        # We return the raw result from the kickoff
        return {"result": result.raw}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

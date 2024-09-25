import pytest  
import requests  
import requests_mock  
import os

api_key = os.getenv("AZURE_API_KEY")
api_version = os.getenv("API_VERSION")
model = os.getenv("MODEL_NAME")
endpoint = os.getenv("AZURE_API_ENDPOINT")
# Assuming the function generate_text_insights is in a file named text_insights.py  
from docu_intel import generate_text_insights  
  
@pytest.fixture  
def mock_text_content():  
    return [  
        {  
            'text': 'This is a sample text for the first slide.',  
            'slide_number': 1,  
            'slide_title': 'Background Information'  
        },  
        {  
            'text': 'This is a sample text for the second slide.',  
            'slide_number': 2,  
            'slide_title': 'Proposal for New System'  
        },  
        {  
            'text': 'This slide has no quality content.',  
            'slide_number': 3,  
            'slide_title': 'Summary'  
        }  
    ]  
  
@pytest.fixture  
def mock_response():  
    return {  
        "choices": [  
            {"message": {"content": "Mock insight for the text."}}  
        ]  
    }  
  
@pytest.fixture  
def api_key():  
    return api_key  
  
@pytest.fixture  
def azure_endpoint():  
    return endpoint
  
@pytest.fixture  
def model():  
    return model 
  
@pytest.fixture  
def api_version():  
    return api_version
  
def test_generate_text_insights_standard(mock_text_content, mock_response, api_key, azure_endpoint, model, api_version):  
    text_length = "Standard"  
  
    with requests_mock.Mocker() as m:  
        m.post(f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}",  
               json=mock_response, status_code=200)  
          
        insights = generate_text_insights(mock_text_content, [], text_length)  
  
        assert len(insights) == len(mock_text_content)  
        for insight in insights:  
            assert 'insight' in insight  
            assert insight['insight'] == "Mock insight for the text."  
  
def test_generate_text_insights_error(mock_text_content, api_key, azure_endpoint, model, api_version):  
    text_length = "Standard"  
  
    with requests_mock.Mocker() as m:  
        m.post(f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}",  
               status_code=500, text="Internal Server Error")  
          
        insights = generate_text_insights(mock_text_content, [], text_length)  
  
        assert len(insights) == len(mock_text_content)  
        for insight in insights:  
            assert 'insight' in insight  
            assert insight['insight'] == "Error in generating insight"  

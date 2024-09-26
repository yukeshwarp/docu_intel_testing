import pytest  
import requests  
import requests_mock  
import os  
from docu_intel import get_image_explanation  # Assuming the function is in the docu_intel module  
  
azure_endpoint = "https://gpt-4omniwithimages.openai.azure.com/"  
api_key = "6e98566acaf24997baa39039b6e6d183"  
api_version = "2024-02-01"  
model = "GPT-40-mini"  
azure_function_url = f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}"  
  
@pytest.fixture  
def mock_response():  
    with requests_mock.Mocker() as m:  
        yield m  
  
def test_get_image_explanation_success(mock_response):  
    base64_image = "iVBORw0KGgoAAAANSUhEUgAA..."  # Example base64 string  
    expected_explanation = "This is a sample explanation of the image content."  
  
    # Mock the successful response from the Azure function  
    mock_response.post(azure_function_url, json={  
        "choices": [  
            {  
                "message": {  
                    "content": expected_explanation  
                }  
            }  
        ]  
    }, status_code=200)  
  
    result = get_image_explanation(base64_image)  
      
    # Check if the function returned the correct explanation  
    assert result == expected_explanation  
  
def test_get_image_explanation_failure(mock_response):  
    base64_image = "iVBORw0KGgoAAAANSUhEUgAA..."  # Example base64 string  
  
    # Mock the failed response from the Azure function  
    mock_response.post(azure_function_url, text="Error", status_code=500)  
  
    result = get_image_explanation(base64_image)  
      
    # Check if the function returned None  
    assert result is None  

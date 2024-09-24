import pytest  
import requests  
import requests_mock  
import json  
  
# Import the function from the module where it is defined  
from docu_intel import generate_image_insights  # replace 'your_module' with the actual module name  
  
def encode_image(image_path):  
    import base64  
    with open(image_path, "rb") as img_file:  
        return base64.b64encode(img_file.read()).decode('utf-8')  
  
@pytest.fixture  
def sample_image_data():  
    return [  
        {  
            "image": "image.png",  
            "slide_number": 1,  
            "slide_title": "Sample Slide 1"  
        },  
        {  
            "image": "image.png",  
            "slide_number": 2,  
            "slide_title": "Sample Slide 2"  
        }  
    ]  
  
@pytest.fixture  
def mock_azure_response():  
    return {  
        "choices": [  
            {  
                "message": {  
                    "content": "This is a test insight for the image."  
                }  
            }  
        ]  
    }  
  
@pytest.fixture  
def api_key():  
    return "6e98566acaf24997baa39039b6e6d183"  
  
@pytest.fixture  
def azure_endpoint():  
    return "https://gpt-4omniwithimages.openai.azure.com/"  
  
@pytest.fixture  
def model():  
    return "GPT4Omni"  
  
@pytest.fixture  
def api_version():  
    return "2024-02-15-preview"  
  
@pytest.fixture  
def text_length():  
    return "Standard"  
  
def test_gti(requests_mock, sample_image_data, mock_azure_response, api_key, azure_endpoint, model, api_version, text_length):  
    # Mock the API response  
    requests_mock.post(f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}", json=mock_azure_response)  
  
    # Encode images  
    for image_data in sample_image_data:  
        image_data['image'] = encode_image(image_data['image'])  
  
    insights, low_quality_slides = generate_image_insights(sample_image_data, text_length, api_key, azure_endpoint, model, api_version)  
  
    # Verify the function returns expected insights  
    assert len(insights) == 2  
    assert insights[0]['slide_number'] == 1  
    assert insights[0]['slide_title'] == "Sample Slide 1"  
    assert insights[0]['insight'] == "This is a test insight for the image."  
      
    assert insights[1]['slide_number'] == 2  
    assert insights[1]['slide_title'] == "Sample Slide 2"  
    assert insights[1]['insight'] == "This is a test insight for the image."  
  
    # Verify there are no low quality slides in this test case  
    assert len(low_quality_slides) == 0  

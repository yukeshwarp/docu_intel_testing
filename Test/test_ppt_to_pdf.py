import pytest  
import requests  
import requests_mock  
import os  
from pathlib import Path  

# Assume the ppt_to_pdf function is defined in a module named ppt_to_pdf_converter  
from docu_intel import ppt_to_pdf  

azure_function_url = "https://doc2pdf.azurewebsites.net/api/HttpTrigger1"


@pytest.fixture  
def mock_response():  
    with requests_mock.Mocker() as m:  
        yield m  
  
def test_ppt_to_pdf_success(mock_response, tmp_path):  
    ppt_file = tmp_path / "temp_ppt.pptx"  
    pdf_file = tmp_path / "temp_pdf.pdf"  
      
    # Create a dummy PPT file  
    ppt_file.write_bytes(b"PPT content")  
      
    # Mock the successful response from the Azure function  
    mock_response.post(azure_function_url, content=b"PDF content", status_code=200)  
      
    result = ppt_to_pdf(ppt_file, pdf_file)  
      
    # Check if the function returned True  
    assert result is True  
      
    # Check if the PDF file is created and has the correct content  
    assert pdf_file.exists()  
    assert pdf_file.read_bytes() == b"PDF content"  
  
def test_ppt_to_pdf_failure(mock_response, tmp_path):  
    ppt_file = tmp_path / "temp_ppt.pptx"  
    pdf_file = tmp_path / "temp_pdf.pdf"  
      
    # Create a dummy PPT file  
    ppt_file.write_bytes(b"PPT content")  
      
    # Mock the failed response from the Azure function  
    mock_response.post(azure_function_url, text="Error", status_code=500)  
      
    result = ppt_to_pdf(ppt_file, pdf_file)  
      
    # Check if the function returned False  
    assert result is False  
      
    # Check if the PDF file was not created  
    assert not pdf_file.exists()  

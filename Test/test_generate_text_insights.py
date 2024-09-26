import pytest  
from unittest.mock import patch, MagicMock  
from io import BytesIO  
from PIL import Image  
import fitz  

from docu_intel import capture_slide_images  # Replace 'your_module' with the actual module name  

@patch("docu_intel.fitz.open")  
@patch("docu_intel.Image.frombytes")  
def test_capture_slide_images(mock_image_frombytes, mock_fitz_open):  
    # Mock the PDF document  
    mock_doc = MagicMock()  
    mock_fitz_open.return_value = mock_doc  
      
    # Mock the pages  
    mock_page = MagicMock()  
    mock_doc.__getitem__.return_value = mock_page  
      
    # Mock the pixmap  
    mock_pix = MagicMock()  
    mock_pix.width = 100  
    mock_pix.height = 200  
    mock_pix.samples = b'\x00' * 100 * 200 * 3  
    mock_page.get_pixmap.return_value = mock_pix  
      
    # Mock the image  
    mock_image = MagicMock()  
    buffer = BytesIO()  
    mock_image.save.side_effect = lambda b, format: b.write(b"fake_image_data")  
    mock_image_frombytes.return_value = mock_image  

    # Define the input  
    pdf_file = "dummy.pdf"  
    slide_numbers = [1, 2, 3]  

    # Call the function  
    images = capture_slide_images(pdf_file, slide_numbers)  

    # Assertions  
    assert len(images) == 3  
    for idx, img in enumerate(images):  
        assert img["slide_number"] == slide_numbers[idx]  
        assert img["image"] == b"fake_image_data"  

    # Verify interactions  
    mock_fitz_open.assert_called_once_with(pdf_file)  
    assert mock_doc.__getitem__.call_count == 3  
    assert mock_page.get_pixmap.call_count == 3  
    assert mock_image_frombytes.call_count == 3  
    assert mock_image.save.call_count == 3  

if __name__ == "__main__":  
    pytest.main()  

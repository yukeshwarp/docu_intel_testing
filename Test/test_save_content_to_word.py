import pytest  
from unittest.mock import patch, MagicMock  
from io import BytesIO  
from docu_intel import save_content_to_word  # Replace 'docu_intel' with the actual module name  
  
@patch("docu_intel.sanitize_text")  
@patch("docu_intel.ensure_proper_spacing")  
@patch("docu_intel.cv2.imencode")  
@patch("docu_intel.Document")  
def test_save_content_to_word(mock_document, mock_cv2_imencode, mock_ensure_proper_spacing, mock_sanitize_text):  
    # Mocking the sanitize_text function  
    mock_sanitize_text.side_effect = lambda x: x  
      
    # Mocking the ensure_proper_spacing function  
    mock_ensure_proper_spacing.side_effect = lambda x: x  
  
    # Mocking the cv2.imencode function  
    mock_cv2_imencode.return_value = (True, b'fake_image_data')  
  
    # Mocking the Document class from python-docx  
    mock_doc_instance = MagicMock()  
    mock_document.return_value = mock_doc_instance  
  
    # Sample data for the function  
    aggregated_content = [  
        {"slide_number": 1, "slide_title": "Slide 1", "content": "Content of slide 1"},  
        {"slide_number": 2, "slide_title": "Slide 2", "content": "Content of slide 2"}  
    ]  
      
    extracted_images = [  
        (b'fake_image_1', 1),  
        (b'fake_image_2', 2)  
    ]  
      
    low_quality_slides = [2]  
      
    output_file_name = "output.docx"  
  
    # Call the function  
    output = save_content_to_word(aggregated_content, output_file_name, extracted_images, low_quality_slides)  
  
    # Assertions  
    assert output is not None  
    assert isinstance(output, BytesIO)  
  
    # Verify that the document was created and saved  
    mock_document.assert_called_once()  
    mock_doc_instance.save.assert_called_once()  
  
    # Verify that headings were added correctly  
    assert mock_doc_instance.add_heading.call_count == len(aggregated_content) + 1  # +1 for "Extracted Images" heading  
  
    # Verify that paragraphs were added correctly  
    expected_paragraph_count = len(aggregated_content) + 1  # +1 for each image paragraph  
    for slide in aggregated_content:  
        if slide['content']:  
            expected_paragraph_count += 1  
    for image, slide_number in extracted_images:  
        if slide_number not in low_quality_slides:  
            expected_paragraph_count += 1  # For the paragraph after the image  
    print(expected_paragraph_count)
    print(mock_doc_instance.add_paragraph.call_count)
    assert mock_doc_instance.add_paragraph.call_count == expected_paragraph_count  
  
    # Verify that pictures were added correctly (excluding low-quality slides)  
    assert mock_doc_instance.add_picture.call_count == len(extracted_images) - len(low_quality_slides)  
  
if __name__ == "__main__":  
    pytest.main()  

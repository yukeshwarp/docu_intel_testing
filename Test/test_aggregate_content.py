import pytest  
from docu_intel import aggregate_content  # Replace 'your_module' with the actual module name  
  
def test_aggregate_content():  
    # Define the input data  
    text_insights = [  
        {"slide_number": 1, "slide_title": "Title 1", "insight": "Text Insight 1"},  
        {"slide_number": 2, "slide_title": "Title 2", "insight": "Text Insight 2"},  
        {"slide_number": 3, "slide_title": "Title 3", "insight": "Text Insight 3"}  
    ]  
  
    image_insights = [  
        {"slide_number": 1, "insight": "Image Insight 1"},  
        {"slide_number": 3, "insight": "Image Insight 3"}  
    ]  
  
    # Expected output  
    expected_output = [  
        {"slide_number": 1, "slide_title": "Title 1", "content": "Image Insight 1"},  
        {"slide_number": 2, "slide_title": "Title 2", "content": "Text Insight 2"},  
        {"slide_number": 3, "slide_title": "Title 3", "content": "Image Insight 3"}  
    ]  
  
    # Call the function  
    result = aggregate_content(text_insights, image_insights)  
  
    # Assertions  
    assert result == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  

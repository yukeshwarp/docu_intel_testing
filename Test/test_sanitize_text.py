import pytest  
from docu_intel import sanitize_text  # Replace 'your_module' with the actual module name  
  
def test_sanitize_text():  
    # Test with a string containing non-printable characters  
    input_text = "Hello\x00World\x1F!"  
    expected_output = "HelloWorld!"  
    assert sanitize_text(input_text) == expected_output  
  
    # Test with a string containing only printable characters  
    input_text = "Hello, World!"  
    expected_output = "Hello, World!"  
    assert sanitize_text(input_text) == expected_output  
  
    # Test with a string containing a mix of printable and non-printable characters  
    input_text = "Good\x07Morning\x1B!"  
    expected_output = "GoodMorning!"  
    assert sanitize_text(input_text) == expected_output  
  
    # Test with an empty string  
    input_text = ""  
    expected_output = ""  
    assert sanitize_text(input_text) == expected_output  
  
    # Test with None  
    input_text = None  
    expected_output = None  
    assert sanitize_text(input_text) == expected_output  
  
    # Test with a string containing only non-printable characters  
    input_text = "\x00\x01\x02\x03"  
    expected_output = ""  
    assert sanitize_text(input_text) == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  

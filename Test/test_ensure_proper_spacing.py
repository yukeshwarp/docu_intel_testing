import pytest  
from docu_intel import ensure_proper_spacing  # Replace 'your_module' with the actual module name  
  
def test_ensure_proper_spacing():  
    # Test with a string with proper spacing  
    input_text = "This is a test. It should work properly."  
    expected_output = "This is a test. It should work properly."  
    assert ensure_proper_spacing(input_text) == expected_output  
  
    # Test with a string with improper spacing (double spaces after periods)  
    input_text = "This is a test.  It should work properly."  
    expected_output = "This is a test. It should work properly."  
    assert ensure_proper_spacing(input_text) == expected_output  
  
    # Test with a string with multiple improper spacings  
    input_text = "This is a test.  It should work properly.  Let's see."  
    expected_output = "This is a test. It should work properly. Let's see."  
    assert ensure_proper_spacing(input_text) == expected_output  
  
    # Test with a string with no periods  
    input_text = "This is a test with no periods"  
    expected_output = "This is a test with no periods"  
    assert ensure_proper_spacing(input_text) == expected_output  
  
    # Test with an empty string  
    input_text = ""  
    expected_output = ""  
    assert ensure_proper_spacing(input_text) == expected_output  
  
    # Test with None  
    input_text = None  
    expected_output = None  
    assert ensure_proper_spacing(input_text) == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  

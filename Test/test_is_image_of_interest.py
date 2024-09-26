import pytest  
from unittest.mock import MagicMock, patch  
import os  
  
# Assuming the is_image_of_interest function is in a module named image_checker  
from docu_intel import is_image_of_interest  
  
@pytest.fixture  
def mock_shape_with_image():  
    mock_shape = MagicMock()  
    mock_image = MagicMock()  
    mock_image.filename = "example.jpg"  
    mock_shape.image = mock_image  
    return mock_shape  
  
@pytest.fixture  
def mock_shape_without_image():  
    mock_shape = MagicMock()  
    mock_shape.image = None  
    return mock_shape  
  
@pytest.fixture  
def mock_shape_with_unsupported_image():  
    mock_shape = MagicMock()  
    mock_image = MagicMock()  
    mock_image.filename = "example.txt"  
    mock_shape.image = mock_image  
    return mock_shape  
  
def test_is_image_of_interest_with_supported_image(mock_shape_with_image):  
    result = is_image_of_interest(mock_shape_with_image)  
    assert result == ".jpg"  
  
def test_is_image_of_interest_without_image(mock_shape_without_image):  
    result = is_image_of_interest(mock_shape_without_image)  
    assert result is None  
  
def test_is_image_of_interest_with_unsupported_image(mock_shape_with_unsupported_image):  
    result = is_image_of_interest(mock_shape_with_unsupported_image)  
    assert result is None  
  
def test_is_image_of_interest_with_exception():  
    mock_shape = MagicMock()  
    mock_shape.image = MagicMock(side_effect=Exception("Error accessing image"))  
    result = is_image_of_interest(mock_shape)  
    assert result is None  

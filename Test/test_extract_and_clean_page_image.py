import pytest
import numpy as np
import cv2
from docu_intel import extract_and_clean_page_image  # Importing the function from docu_intel

# Mock page object and related methods
class MockPixmap:
    def __init__(self, image_array):
        self.samples = image_array.tobytes()
        self.height, self.width, self.n = image_array.shape

class MockPage:
    def __init__(self, image_array):
        self.pixmap = MockPixmap(image_array)

    def get_pixmap(self):
        return self.pixmap

# Test function
def test_extract_and_clean_page_image():
    # Create a mock image with some drawings and text
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White background
    cv2.rectangle(img, (10, 10), (90, 40), (0, 0, 0), -1)  # Black rectangle (simulating text or drawing)
    cv2.rectangle(img, (10, 60), (90, 90), (0, 0, 0), 2)  # Black border rectangle (simulating a diagram)

    # Create a mock page
    page = MockPage(img)

    # Run the function with some masking values
    cleaned_image_gray = extract_and_clean_page_image(page, top_mask=5, bottom_mask=5, left_mask=5, right_mask=5)

    # Assert that the result is not None
    assert cleaned_image_gray is not None, "The cleaned image should not be None."

    # Assert that the cleaned image is not all white (i.e., something was detected)
    assert not np.all(cleaned_image_gray == 255), "The cleaned image should not be all white; it should contain detected contours."

    # Optionally, you can add more specific checks, such as comparing with expected output

# Running the test with pytest
if __name__ == "__main__":
    pytest.main([__file__])

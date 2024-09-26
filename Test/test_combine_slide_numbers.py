import pytest  
  
# Assuming the combine_slide_numbers function is in a module named ppt_combiner  
from docu_intel import combine_slide_numbers  
  
#def combine_slide_numbers(image_slides, visual_slides):  
#    """Combine slide numbers from image slides and visual element slides"""  
#    combined_slides = set(image_slides.keys()).union(set(visual_slides))  
#    return sorted(list(combined_slides))  
  
def test_combine_slide_numbers():  
    # Test Case 1: Both image_slides and visual_slides have entries  
    image_slides = {1: ".jpg", 3: ".png"}  
    visual_slides = [2, 3, 4]  
    expected = [1, 2, 3, 4]  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
    # Test Case 2: image_slides is empty  
    image_slides = {}  
    visual_slides = [2, 3, 4]  
    expected = [2, 3, 4]  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
    # Test Case 3: visual_slides is empty  
    image_slides = {1: ".jpg", 3: ".png"}  
    visual_slides = []  
    expected = [1, 3]  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
    # Test Case 4: Both image_slides and visual_slides are empty  
    image_slides = {}  
    visual_slides = []  
    expected = []  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
    # Test Case 5: Overlapping slide numbers in image_slides and visual_slides  
    image_slides = {1: ".jpg", 2: ".png"}  
    visual_slides = [2, 3]  
    expected = [1, 2, 3]  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
    # Test Case 6: Non-overlapping slide numbers in image_slides and visual_slides  
    image_slides = {1: ".jpg", 4: ".png"}  
    visual_slides = [2, 3]  
    expected = [1, 2, 3, 4]  
    assert combine_slide_numbers(image_slides, visual_slides) == expected  
  
if __name__ == "__main__":  
    pytest.main()  

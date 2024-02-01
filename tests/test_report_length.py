from lib.report_length import *

def test_report_length():
    assert report_length("Hello") == "This string was 5 characters long"
    assert report_length("Goodbye") == "This string was 7 characters long"
    assert report_length("How are you?") == "This string was 12 characters long"
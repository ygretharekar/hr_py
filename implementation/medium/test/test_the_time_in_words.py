"""Test for the time in word"""
from .. import the_time_in_words

def test_solution():
    "test"
    t_w = the_time_in_words.TheTimeInWords()
    assert t_w.solution(5, 0) == "five o' clock"

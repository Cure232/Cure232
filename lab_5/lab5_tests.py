import pytest

from main import read_txt
from old_tests import frequency_bit_test, consecutive_bits_test, longest_sequence_test

@pytest.mark.parametrize("input_text, expected_result", [
    ("111", 0.08326451666355043), ("0110110", 0.7054569861112734),
    ("010101", 1), ("101010", 1), 
])
def test_frequency_bit_test(input_text, expected_result):
    result = frequency_bit_test(input_text)
    assert abs(result - expected_result) < 0.05


def test_identical_consecutive_bits1():
    input_text = "101010"
    result = consecutive_bits_test(input_text)
    assert result == 0.10247043485974938
    

def test_identical_consecutive_bits2():
    input_text = "111111"
    result = consecutive_bits_test(input_text)
    assert result == 0


def test_identical_consecutive_bits3():
    input_text = "0110110"
    result = consecutive_bits_test(input_text)
    assert result == 0.6592430036926307
    

def test_identical_consecutive_bits4():
    input_text = "010101"
    result = consecutive_bits_test(input_text)
    assert result == 0.10247043485974938

    
@pytest.mark.parametrize("input_text, expected_result", [
    ("1"*128, 0),
    ("0"*128, 0),
    (read_txt("resources/cpp_sequence.txt"), 0.4),
    (read_txt("resources/java_sequence.txt"), 0.25),
])
def test_longest_sequence_test(input_text, expected_result):
    result = longest_sequence_test(input_text)
    assert abs(result - expected_result) < 0.05

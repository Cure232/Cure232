import pytest

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
    ("00110111100000100011011101001111001100100111000100000011101001101101110100000101011000000011100010000111000001000001111011111000", 0.4),
    ("11001001110000101010011100010101101101101001100111001011000111010110100111001100010110100011010100101111111111000001110000010111", 0.25),
])  #Сначала CPP, потом Java.
def test_longest_sequence_test(input_text, expected_result):
    result = longest_sequence_test(input_text)
    assert abs(result - expected_result) < 0.05


def test_longest_sequence_crash_test1():
    with pytest.raises(ValueError, match="This test is designed for 128 bits long string"):
        result = longest_sequence_test("100")
    

def test_longest_sequence_crash_test2():
    with pytest.raises(ValueError, match="This is not a bitstring"):
        result = longest_sequence_test("404not a bit string")
    

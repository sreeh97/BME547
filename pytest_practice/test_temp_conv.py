def test_celcius_from_fahrenheit():
	from temp_conv import celsius_from_fahrenheit
	result = celsius_from_fahrenheit(20)
	expected = 68
	assert result == expected

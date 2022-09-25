import pytest

@pytest.mark.parametrize("HDL, expected",
    [(85,"Normal"),
     (50, "Borderline Low"),
     (30, "Low")
     ])
def test_check_HDL(HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL)
    assert answer == expected


@pytest.mark.parametrize("LDL, expected",
    [(100,"Normal"),
     (140, "Borderline High"),
     (170, "High"),
     (210, "Very High")
     ])

def test_check_LDL(LDL, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL)
    assert answer == expected
   
   
@pytest.mark.parametrize("Total, expected",
    [(150,"Normal"),
     (220, "Borderline high"),
     (270, "High"),
     ])

def test_Total_check(Total, expected):
    from blood_calculator import Total_check
    answer = Total_check(Total)
    assert answer == expected


"""   
   answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected
    answer = check_HDL(30)
    expected = "Low"
    assert answer == expected
    

def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected
    

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(30)
    expected = "Low"
    assert answer == expected
"""
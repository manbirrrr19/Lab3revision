import lab2revision.bmi as bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(height=1.73, weight=57) == 0)
def test_bmi_over_weight():
    assert(bmi.calculate_bmi(height=1.73, weight=57) == 1)
def test_bmi_under_weight():
    assert(bmi.calculate_bmi(height=1.73, weight=57) == -1)


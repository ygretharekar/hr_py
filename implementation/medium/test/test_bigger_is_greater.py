"""test bigger is greater"""
from .. import bigger_is_greater
#ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl
#ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl


def test_solution():
    """Test solution"""
    b_g = bigger_is_greater.BiggerIsGreater()
    # inp_a = "biehzcmjckznhwrfgglverxsezxuqpj"
    # inp_b = "biehzcmjckznhwrfgglverxsjepquxz"
    inp_a = "ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl"
    inp_b = "ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl"
    assert b_g.solution(inp_a) == inp_b

def test_editorial_solution():
    """Test solution"""
    b_g = bigger_is_greater.BiggerIsGreater()
    inp_a = "ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl"
    inp_b = "ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvl"
    assert b_g.editorial_solution(inp_a) == inp_b

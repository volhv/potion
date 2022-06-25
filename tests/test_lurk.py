from potion.util.files import Lurk
 

def test_lurk():
    
    lk = Lurk(".")
    assert "tests" in set(lk.ls())
    
    rz = set(lk.rls("tests/test_{test_name:str}/"))
        
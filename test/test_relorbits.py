#!/usr/local/bin/python3

# Test Modules
import sys
import pytest
import logging
from   pytest import approx
from   os     import path
import math
import numpy as np
import copy

# Import module undera test
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
# Set Log level
LOG_FORMAT = '%(levelname)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

# Import modules for testing
from brahe.constants import *
from brahe.epoch     import *
from brahe.orbits    import sOSCtoCART
from brahe.relorbits import *

# Test main code

def test_rtn_rotations():
    epc = Epoch(2018,1,1,12,0,0)

    a   = R_EARTH + 500e3
    oe  = [a, 0, 0, 0, 0, math.sqrt(GM_EARTH/a)]
    eci = sOSCtoCART(oe, use_degrees=True)

    r_rtn   = rRTNtoECI(eci)
    r_rtn_t = rECItoRTN(eci)

    np.testing.assert_almost_equal(r_rtn, r_rtn_t.T, decimal=8)

def test_rtn_states(): 
    epc = Epoch(2018,1,1,12,0,0)

    oe  = [R_EARTH + 500e3, 0, 0, 0, 0, 0]
    eci = sOSCtoCART(oe, use_degrees=True)

    xt = copy.deepcopy(eci) + [100, 0, 0, 0, 0, 0]

    x_rtn = sECItoRTN(eci, xt)

    tol = 1e-8
    assert approx(x_rtn[0], 100.0, abs=tol)
    assert approx(x_rtn[1], 0.0, abs=tol)
    assert approx(x_rtn[2], 0.0, abs=tol)
    assert approx(x_rtn[3], 0.0, abs=tol)
    assert approx(x_rtn[4], 0.0, abs=0.5)
    assert approx(x_rtn[5], 0.0, abs=tol)

    xt2 = sRTNtoECI(eci, x_rtn)

    assert approx(xt[0], xt2[0], abs=tol)
    assert approx(xt[1], xt2[1], abs=tol)
    assert approx(xt[2], xt2[2], abs=tol)
    assert approx(xt[3], xt2[3], abs=tol)
    assert approx(xt[4], xt2[4], abs=tol)
    assert approx(xt[5], xt2[5], abs=tol)

if __name__ == '__main__':
    test_rtn_rotations()
    test_rtn_states()
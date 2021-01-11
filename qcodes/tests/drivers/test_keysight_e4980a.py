import pytest
import qcodes.instrument_drivers.Keysight.keysight_e4980a as E4980A

import qcodes.instrument.sims as sims

VISALIB = sims.__file__.replace('__init__.py', 'Keysight_E4980A.yaml@sim')

# pylint: disable=redefined-outer-name
@pytest.fixture
def driver():
    instr = E4980A.KeysightE4980A('E4980A',
                                  address="GPIB::1::INSTR",
                                  visalib=VISALIB)
    yield instr
    instr.close()


def test_idn(driver):
    assert {'firmware': 'A.02.10',
            'model': 'E4980A',
            'serial': '1000',
            'vendor': 'Keysight'} == driver.IDN()

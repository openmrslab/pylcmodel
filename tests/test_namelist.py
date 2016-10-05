import pylcmodel


def test_integer():
    assert 1 == pylcmodel.namelist.parser("1").number()


def test_float():
    assert 2.3 == pylcmodel.namelist.parser("2.3").number()


def test_exponent():
    assert 1.2e4 == pylcmodel.namelist.parser("1.2e4").number()


def test_negative():
    assert -7.9 == pylcmodel.namelist.parser("-7.9").number()


def test_numberlist():
    assert [1, 2, 3.4] == pylcmodel.namelist.parser("1 2 3.4").numberlist()


def test_strings():
    assert "hello world" == pylcmodel.namelist.parser("'hello world'").string()


def test_unquoted_string():
    assert "helloworld" == pylcmodel.namelist.parser("helloworld\n").string()


def test_string_list():
    assert ["hello", "world"] == pylcmodel.namelist.parser("'hello' 'world'").stringlist()


def test_truth():
    assert pylcmodel.namelist.parser("T").truth()


def test_falsehood():
    assert not pylcmodel.namelist.parser("F").falsehood()


def test_key_value_pair():
    assert ("KEY", "value") == pylcmodel.namelist.parser("key = 'value'").pair()


def test_pairlist():
    assert [("KEY", "value")] == pylcmodel.namelist.parser("key = 'value'").pairlist()


def test_namelist():
    namelist_string = """
    $name
     key='value'
     unquoted = test,
     other=2.3
    $END
    """.strip()
    target = ("name",
              {"KEY": "value", "OTHER": 2.3, "UNQUOTED": "test"})
    assert target == pylcmodel.namelist.parser(namelist_string).namelist()


def test_namelist_two():
    namelist_string = """
    $name
     SPTYPE = liver-11 ,
    $END
    """.strip()
    assert ("name", {"SPTYPE": "liver-11"}) == pylcmodel.namelist.parser(namelist_string).namelist()


def test_control_file():
    with open("tests/test_data/lcm.control") as fin:
        control_file_text = fin.read()
    assert ("LCMODL", {
        "KEY": 123456789,
        "LCSV": 11,
        "OWNER": "",
        "FILTAB": "test_data/svs_97.TABLE",
        "DELTAT": 0.000833,
        "NUNFIL": 1024,
        "HZPPPM": 123.226103,
        "LCOORD": 9,
        "TITLE": "SVS_97",
        "FILRAW": "test_data/svs_97.RAW",
        "LTABLE" :7,
        "FILCSV": "test_data/svs_97.CSV",
        "FILBAS": "/media/mrs_proc/ben/97ms demo/LCModel files/97_basis_set.basis",
        "FILPS": "test_data/svs_97.PS",
        "FILCOO": "test_data/svs_97.COORD"
    }) == pylcmodel.namelist.reads(control_file_text.strip())


def test_write_number():
    target = """ $LCMODL
 NUM = 4,
 $END
"""
    assert target == pylcmodel.namelist.dumps("LCMODL", {"NUM": 4})


def test_write_string():
    target = """ $LCMODL
 STR = 'test',
 $END
"""
    assert target == pylcmodel.namelist.dumps("LCMODL", {"STR": "test"})


def test_write_truth():
    target = """ $LCMODL
 TRUE = T,
 $END
"""
    assert target == pylcmodel.namelist.dumps("LCMODL", {"TRUE": True})


def test_write_falsehood():
    target = """ $LCMODL
 FALSE = F,
 $END
"""
    assert target == pylcmodel.namelist.dumps("LCMODL", {"FALSE": False})

from copy import deepcopy

from wireviz_web.core import mimetype_type_map
from wireviz_web.util import ReversibleDict


def test_reversible_dict():
    rdict = ReversibleDict(mimetype_type_map)

    rdict["foo/bar"] = "bazqux"
    assert "foo/bar" in rdict

    del rdict["image/png"]
    assert "image/png" not in rdict

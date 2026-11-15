import pytest

from baseline.tasks import first_missing


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_the_first_required_item_that_is_absent():
    assert first_missing(["a", "b", "c"], ["a"]) == "b"
from pycbc_examples.examples import loading_data


class TestExampleLoadingData:
    def test_get_catalogs(self):
        mergers = loading_data.get_mergers()
        assert len(mergers) == 11

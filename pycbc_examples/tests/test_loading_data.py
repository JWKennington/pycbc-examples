from gravtools import time, MergerParameters, Observatory

from pycbc import catalog


class TestExampleLoadingData:
    """These tests mostly check that the notebook will run,
    by running the same code. In the future this can be cleaned
    up by using nbconvert to automatically convert the notebook
    into python code.
    """

    def test_catalog(self):
        cat = catalog.Catalog(source='gwtc-1')

    def test_mergers(self):
        cat = catalog.Catalog(source='gwtc-1')
        merger_names = list(cat)  # Catalog class is iterable, any collection coercion will suffice
        labels = [
            'GW150914: M1=36 M2=31 z=0.09',
            'GW151012: M1=23 M2=14 z=0.21',
            'GW151226: M1=14 M2=8 z=0.09',
            'GW170104: M1=31 M2=20 z=0.19',
            'GW170608: M1=11 M2=8 z=0.07',
            'GW170729: M1=51 M2=34 z=0.48',
            'GW170809: M1=35 M2=24 z=0.20',
            'GW170814: M1=31 M2=25 z=0.12',
            'GW170817: M1=1 M2=1 z=0.01',
            'GW170818: M1=36 M2=27 z=0.20',
            'GW170823: M1=40 M2=29 z=0.34',
        ]

        for i, name in enumerate(merger_names):
            m = cat.mergers[name]
            formatted = '{}: M1={:.0f} M2={:.0f} z={:.2f}'.format(name,
                                                                  m.median1d(MergerParameters.Mass1),  # m.mass1
                                                                  m.median1d(MergerParameters.Mass2),  # m.mass2
                                                                  m.median1d(MergerParameters.Redshift))
            assert labels[i] == formatted

    def test_strain(self):
        m = catalog.Merger('GW170823')
        ts = m.strain(ifo=Observatory.LIGOHanford)
        detail_str = 'Duration={:.0f}s Interval={:.1e}s Start={} End={}'.format(ts.duration, ts.delta_t,
                                                                                time.gps_to_datetime(ts.start_time),
                                                                                time.gps_to_datetime(ts.end_time))
        assert detail_str == 'Duration=32s Interval=2.4e-04s Start=2017-08-23 13:14:20 End=2017-08-23 13:14:52'

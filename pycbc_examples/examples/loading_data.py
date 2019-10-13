import enum

from pycbc import catalog, frame


class MergerParameters(enum.Enum):
    """Useful enumeration of Merger class parameters. These parameters
    get set using setattr, so code inspection doesn't work naturally - this
    Enum can help recall the attributes in an inspectable way.
    """
    ChirpMass = 'mchirp'
    EffInspiralSpin = 'chi_eff'
    FinalMass = 'mfinal'
    FinalSpin = 'a_final'
    LuminosityDistance = 'distance'
    Mass1 = 'mass1'
    Mass2 = 'mass2'
    PeakLuminosity = 'L_peak'
    RadiatedEnergy = 'E_rad'
    Redshift = 'redshift'
    SkySize = 'sky_size'
    SignalNoiseRatio_CWB = 'snr_cwb'
    SignalNoiseRatio_GSTLAL = 'snr_gstlal'
    SignalNoiseRatio_PYCBC = 'snr_pycbc'


class Observatory(enum.Enum):
    """Helpful enumeration of observatories for loading strain data"""
    LIGOHanford = 'H1'
    LIGOLivingston = 'L1'
    VIRGO = 'V1'


def ex_1_explore_catalog():
    """This example shows how to explore the Catalog of available Mergers. Currently, the list of available
    Mergers can be found at the following url: https://www.gw-openscience.org/catalog/GWTC-1-confident/html/.

    PyCBC has a Catalog class that is capable of using the GWOSC data api to see essentially the same information
    contained in the link above (albeit through JSON instead of HTML). Under the hood, PyCBC relies on AstroPy
    data access file download utilities.

    The Catalog class is iterable, so you can pick your favorite technique to iterate over the available
    Mergers in the GWOSC center (we use the list coercion function below).

    Each Merger object has several parameters set, though they are not inspectable since they are set using
    "setattr". The Enum above contains constants associated to these attributes. Each attribute may be
    accessed directly, but the preferred way is through the "median1d" method of the Merger class. Keep
    in mind that these parameters are in the *source* frame, not the *detector* frame.

    Examples:
        >>> ex_1_explore_catalog()
        Mergers in catalog:
            GW150914: M1=36 M2=31 z=0.09
            GW151012: M1=23 M2=14 z=0.21
            GW151226: M1=14 M2=8 z=0.09
            GW170104: M1=31 M2=20 z=0.19
            GW170608: M1=11 M2=8 z=0.07
            GW170729: M1=51 M2=34 z=0.48
            GW170809: M1=35 M2=24 z=0.20
            GW170814: M1=31 M2=25 z=0.12
            GW170817: M1=1 M2=1 z=0.01
            GW170818: M1=36 M2=27 z=0.20
            GW170823: M1=40 M2=29 z=0.34
    """
    # The "source" argument below refers to the Gravitational-Wave Transient Catalog 1
    # (Compact Binary Mergers oberved in O1 and O2).
    cat = catalog.Catalog(source='gwtc-1')

    # Get names of mergers in catalog - all merger data is keyed by name in the "mergers" dict
    merger_names = list(cat)  # Catalog class is iterable, any collection coercion will suffice

    # Log the names of the mergers in the catalog
    print('Mergers in catalog:')
    for name in merger_names:
        m = cat.mergers[name]

        # Print some merger info by accessing parameters through the "median1d" method
        print('    {}: M1={:.0f} M2={:.0f} z={:.2f}'.format(name,
                                                            m.median1d(MergerParameters.Mass1.value),     # m.mass1
                                                            m.median1d(MergerParameters.Mass2.value),     # m.mass2
                                                            m.median1d(MergerParameters.Redshift.value))) # m.redshift


def ex_2_merger_strain():
    """A Merger object loads several scalar parameters once instantiated, however, it is also
    possible to load the strain timeseries around the event. The time series data will be return
    as an instance of pycbc.types.timeseries.TimeSeries, which is a thin wrapper around a numpy
    or pycuda array with additional metadata. This example shows how to load the data and how to
    do some useful manipulations.

    Examples:
        >>> ex_2_merger_strain()
        Duration=32s Interval=2.4e-04s Start=1187529241 End=1187529273
    """
    # Pick a merger from the catalog
    m = catalog.Merger('GW170823')

    # Query the strain timeseries for the merger
    ts = m.strain(ifo=Observatory.LIGOHanford.value) # the "ifo" argument refers to the observatory that recorded the strain

    # Print the boundaries of the timeseries
    print('Duration={:.0f}s Interval={:.1e}s Start={} End={}'.format(ts.duration, ts.delta_t, ts.start_time, ts.end_time))


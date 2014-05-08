About
-----

A simple package to represent flux measurements

Example
-------

We can start off by reading in a file containing JSON-encoded data on each row:

    >>> from flux_measurement import MeasurementSet
    >>> all = MeasurementSet.from_file('example_data')
    >>> all
    [<Measurement source_id=source_000 flux=8.603303604760317 wavelength=3.6 object_id=0>,
     <Measurement source_id=source_000 flux=1.021605304728429 wavelength=4.5 object_id=3>,
     <Measurement source_id=source_000 flux=4.036046818717632 wavelength=5.8 object_id=3>,
     <Measurement source_id=source_000 flux=0.5973233320011062 wavelength=8.0 object_id=5>,
     <Measurement source_id=source_001 flux=1.5614452604523954 wavelength=3.6 object_id=4>,
     ...
     <Measurement source_id=source_018 flux=4.21870552880097 wavelength=5.8 object_id=9>,
     <Measurement source_id=source_018 flux=2.2039536931085104 wavelength=8.0 object_id=2>,
     <Measurement source_id=source_019 flux=3.049518194637848 wavelength=4.5 object_id=9>,
     <Measurement source_id=source_019 flux=1.151675424448243 wavelength=5.8 object_id=4>,
     <Measurement source_id=source_019 flux=3.9462547104421617 wavelength=8.0 object_id=1>]

We can access individual measurements:

    >>> m = all[0]

    >>> m.source_id
    'source_000'

    >>> m.flux
    8.603303604760317

We can also apply selections to mesaurement sets:

    >>> subset1 = all.select(all.object_id==1)
    >>> subset1
    [<Measurement source_id=source_002 flux=7.890218635385256 wavelength=3.6 object_id=1>,
     <Measurement source_id=source_003 flux=8.581521784485677 wavelength=8.0 object_id=1>,
     <Measurement source_id=source_005 flux=4.414947900893139 wavelength=4.5 object_id=1>,
     <Measurement source_id=source_014 flux=7.432635032684938 wavelength=5.8 object_id=1>,
     <Measurement source_id=source_015 flux=6.986826970697097 wavelength=4.5 object_id=1>,
     <Measurement source_id=source_019 flux=0.2014576415530689 wavelength=3.6 object_id=1>,
     <Measurement source_id=source_019 flux=3.9462547104421617 wavelength=8.0 object_id=1>]

    >>> subset2 = all.select((all.object_id==1) & (all.flux > 3.))
    >>> subset2
    [<Measurement source_id=source_002 flux=7.890218635385256 wavelength=3.6 object_id=1>,
     <Measurement source_id=source_003 flux=8.581521784485677 wavelength=8.0 object_id=1>,
     <Measurement source_id=source_005 flux=4.414947900893139 wavelength=4.5 object_id=1>,
     <Measurement source_id=source_014 flux=7.432635032684938 wavelength=5.8 object_id=1>,
     <Measurement source_id=source_015 flux=6.986826970697097 wavelength=4.5 object_id=1>,
     <Measurement source_id=source_019 flux=3.9462547104421617 wavelength=8.0 object_id=1>]
     
As shown in the selections above, accessing attributes on the measurement set
that are measurement properties, we get an array containing all the values for
that attribute for all measurements (and ``None`` if the measurement does not
contain that attribute):
    
     In [5]: subset2.flux
     Out[5]: 
     array([ 7.89021864,  8.58152178,  4.4149479 ,  7.43263503,  6.98682697,
             3.94625471])

     In [6]: subset2.source_id
     Out[6]: 
     array(['source_002', 'source_003', 'source_005', 'source_014',
            'source_015', 'source_019'], 
           dtype='<U10')
           
We can also write the measurement set back out to a file:

    >>> subset2.to_file('example_subset')

And the resulting file looks like:

    {"flux":7.890218635385256,"object_id":1,"source_id":"source_002","wavelength":3.6}
    {"flux":8.581521784485677,"object_id":1,"source_id":"source_003","wavelength":8.0}
    {"flux":4.414947900893139,"object_id":1,"source_id":"source_005","wavelength":4.5}
    {"flux":7.432635032684938,"object_id":1,"source_id":"source_014","wavelength":5.8}
    {"flux":6.986826970697097,"object_id":1,"source_id":"source_015","wavelength":4.5}
    {"flux":3.9462547104421617,"object_id":1,"source_id":"source_019","wavelength":8.0}

Flexibility
-----------

The idea behind these classes and the JSON storage is flexibility in terms of
the data contained for each measurement. Only the properties used are stored.

As an example of flexibility, we can store a source along with the polygon that
defines it spatially:

    >>> from flux_measurement import Measurement
    >>> m = Measurement()
    >>> m.source_id = "extended_source"
    >>> m.shape = 'polygon'
    >>> m.polygon = [(1.,3.), (4., 3.), (2., 5.)]
    >>> m.to_json()
    '{"shape":"polygon","polygon":[[1.0,3.0],[4.0,3.0],[2.0,5.0]],"source_id":"extended_source"}'

Caveats
-------

This is not intended for storing large catalogs with more 10^6 or more sources.
For high performance, we could consider storing the data in FITS binary table
form instead, since we can still use variable length vector columns for things
like shape lists, etc.

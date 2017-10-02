CSV_Play.py
-----------

Python script for simple playback of DMX values over the network.


Usage:
python CSVPlay.py <CSV_Data> <universe number>

e.g. 'python CSVPlay.py test.csv 1'



Required setup - 

Python 2.7


Files:
	CSV_Play.py
	packet.py
	source.py
	
Also, the data file you want would like to play out. 
This file should contain up to 512 comma separates values on each line. 
Each line represents a packet (or loosely, a frame)






This code is based on the Lumos python library. The readme for this is below

Lumos: a pure Python E1.31 library
==================================

Lumos is a Python library for working with DMX512_ lighting control signals sent over ethernet. 
This is done using multicast UDP as a sub-protocol of ACN referred to as E1.31 or streaming ACN.

.. _DMX512: http://en.wikipedia.org/wiki/DMX512
.. _ACN: http://en.wikipedia.org/wiki/Architecture_for_Control_Networks

This is currently only an implementation of basic transmit functionality.

Usage
-----

The entirety of the current functionality is exposed through a single class::

    from lumos import DMXSource

    source = DMXSource(universe=1)

    # data is an iterable of DMX512 bytes
    data = [255] * 50

    source.send_data(data)

For a far more complete tool see the `OLA project`_ - but for smaller, more
portable projects, this library may be all you need.

.. _`OLA project`: http://opendmx.net/index.php/OLA

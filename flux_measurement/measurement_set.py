import numpy as np
from .measurement import Measurement


class MeasurementSet(object):
    """
    A set of measurements that can be queried
    """

    def __init__(self, measurements=None):
        if measurements is None or isinstance(measurements, (list, set, tuple)):
            self._measurements = measurements
        else:
            raise TypeError("measurements should be a list, set, or tuple")

    def to_file(self, filename):
        with open(filename, 'w') as f:
            for m in self._measurements:
                f.write(m.to_json())
                f.write("\n")

    @classmethod
    def from_file(cls, filename):
        measurements = []
        for line in open(filename):
            if line.strip() == "":
                continue
            measurements.append(Measurement.from_json(line))
        return cls(measurements=measurements)

    def __getattr__(self, attr):
        if hasattr(Measurement, attr):
            return np.array([getattr(m, attr, None) for m in self._measurements])
        else:
            raise AttributeError("MeasurementSet has no attribute: {0}".format(attr))

    def select(self, keep):
        if len(keep) != len(self._measurements):
            raise ValueError("Length of selection should match number of measurements")
        subset = []
        for i in range(len(keep)):
            if keep[i]:
                subset.append(self._measurements[i])
        return MeasurementSet(measurements=subset)

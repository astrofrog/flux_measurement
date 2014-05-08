import numpy as np
from .measurement import Measurement


class MeasurementSet(list):
    """
    A set of measurements that can be queried
    """

    def to_file(self, filename):
        with open(filename, 'w') as f:
            for m in self:
                f.write(m.to_json())
                f.write("\n")

    @classmethod
    def from_file(cls, filename):
        self = cls()
        for line in open(filename):
            if line.strip() == "":
                continue
            self.append(Measurement.from_json(line))
        return self

    def __getattr__(self, attr):
        if hasattr(Measurement, attr):
            return np.array([getattr(m, attr, None) for m in self])
        else:
            raise AttributeError("MeasurementSet has no attribute: {0}".format(attr))

    def select(self, keep):
        if len(keep) != len(self):
            raise ValueError("Length of selection should match number of measurements")
        subset = MeasurementSet()
        for i in range(len(keep)):
            if keep[i]:
                subset.append(self[i])
        return subset

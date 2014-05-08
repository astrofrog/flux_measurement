import json


class Measurement(object):

    def __init__(self, flux=None, wavelength=None, filter=None, epoch=None,
                 position=None, shape=None, object_id=None):

        self.flux = flux
        self.wavelength = wavelength
        self.filter = filter
        self.epoch = epoch
        self.position = position
        self.shape = shape
        self.object_id = object_id

    @property
    def flux(self):
        return self._flux

    @flux.setter
    def flux(self, value):
        self._flux = value

    @property
    def wavelength(self):
        return self._wavelength

    @wavelength.setter
    def wavelength(self, value):
        self._wavelength = value

    @property
    def filter(self):
        return self._filter

    @filter.setter
    def filter(self, value):
        self._filter = value

    @property
    def epoch(self):
        return self._epoch

    @epoch.setter
    def epoch(self, value):
        self._epoch = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        if value is None or value in ['gaussian', 'circle', 'polygon']:
            self._shape = value
        else:
            raise ValueError("shape should be one of gaussian/circle/polygon")

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    def to_json(self):
        data = {}
        for attr in ['flux', 'wavelength', 'filter', 'epoch', 'position',
                     'shape', 'object_id']:
            value = getattr(self, attr)
            if value is None:
                continue
            data[attr] = value
        return json.dumps(data, separators=(',', ':'))

    @classmethod
    def from_json(cls, string):
        data = json.loads(string)
        return cls(**data)

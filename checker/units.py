"""Units used throughout the Earth Engine catalog.

Mirrors the units listed here:

https://github.com/google/earthengine-catalog/blob/main/catalog/units.libsonnet
"""

# TODO(schwehr): Load this from units.libsonnet
UNITS = frozenset({
    '%',
    '% change/y',
    '1/s',
    'Area fraction',
    'Dimensionless',
    'Mass fraction',
    'Mol fraction',
    'Fraction',
    'Volume fraction',
    'Dobson',
    'GHz',
    'Gg',
    'J/kg',
    'J/m^2',
    'K',
    'nmi',
    'MW',
    'Mg/ha',
    'N/m^2',
    'Pa',
    'Pa s',
    'P-value',
    'W/m^2',
    'y',
    'atm cm',
    'cm',
    'count',
    'count/d',
    'count/acre',
    'c%/a',
    'd',
    'dB',
    'deg',
    'dn',
    'ft',
    'ft^2',
    'ft^2/acre',
    'ft^3/acre',
    'gpm',
    'h',
    'h/km^2',
    'ha',
    'hPa',
    'in',
    'kg/h',
    'kg/h/km^2',
    'kg/m^2',
    'kg/m^2/s',
    'kg/m^3',
    'kPa',
    'km',
    'km^2',
    'kt',
    'm',
    'm/s',
    'm/s^2',
    'm^2',
    'mbar',
    'mg/m^3',
    'min',
    'mm',
    'mm/d',
    'mm/y',
    'nanoWatts/sr/cm^2',
    'nm',
    'pixel',
    'ppb',
    'ppm',
    'psu',
    'rad',
    'sawlog-board-ft/acre',
    'seconds',
    'tons/acre',
    '&deg;C',
    '&deg;F',
    '&micro;m',
    '&mu;g/m&sup3',
    '&mu;m',
})

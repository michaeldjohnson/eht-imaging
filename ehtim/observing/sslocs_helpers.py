from astropy.time import Time
from astropy.coordinates import EarthLocation, get_body
from astropy.constants import M_sun, M_earth, au
import astropy.units as units
import numpy as np


##############################################################################
#DEFINE USEFUL CONSTANTS in kg, m, s
##############################################################################
Msun = M_sun.to_value(units.kg)
Mearth = M_earth.to_value(units.kg)
Mmoon = 7.34767309e22
#Sun-Earth Hill factor
SEH = (Mearth / (3*Msun))**(1/3)
#Earth-Moon Hill factor
MEH = (Mmoon / (3*Mearth))**(1/3)
EARTHCORE = EarthLocation.from_geocentric(0,0,0,'m')


##############################################################################
#COMPUTING FUNCTIONS
##############################################################################

#TODO: implement the rest of the lagrange points, and then update SSLOCS in const_def.py

def SEL1(time):
    """
    Computes the position of Sun-Earth L1 in geocentric coordinates at the given time.
    """
    sun = get_body('sun', time, EARTHCORE)
    sc = sun.represent_as('cartesian')
    scx = sc.x.to_value(units.m)
    scy = sc.y.to_value(units.m)
    scz = sc.z.to_value(units.m)
    vec =  (SEH*scx, SEH*scy, SEH*scz)
    return vec


def SEL2(time):
    """
    Computes the position of Sun-Earth L2 in geocentric coordinates at the given time.
    """
    sun = get_body('sun', time, EARTHCORE)
    sc = sun.represent_as('cartesian')
    scx = sc.x.to_value(units.m)
    scy = sc.y.to_value(units.m)
    scz = sc.z.to_value(units.m)
    vec =  (-SEH*scx, -SEH*scy, -SEH*scz)
    return vec



def EML1(time):
    """
    Computes the position of Earth-Moon L1 in geocentric coordinates at the given time.
    """

    moon = get_body('moon', time, EARTHCORE)
    mc = moon.represent_as('cartesian')
    mcx = mc.x.to_value(units.m)
    mcy = mc.y.to_value(units.m)
    mcz = mc.z.to_value(units.m)
    vec = (mcx-MEH*mcx, mcy-MEH*mcy, mcz-MEH*mcz)
    return vec


def EML2(time):
    """
    Computes the position of Earth-Moon L2 in geocentric coordinates at the given time.
    """
    moon = get_body('moon', time, EARTHCORE)
    mc = moon.represent_as('cartesian')
    mcx = mc.x.to_value(units.m)
    mcy = mc.y.to_value(units.m)
    mcz = mc.z.to_value(units.m)
    vec = (mcx+MEH*mcx, mcy+MEH*mcy, mcz+MEH*mcz)
    return vec



##############################################################################
#DICTIONARY OF NAMES TO FUNCTIONS
##############################################################################

FUNCDICT = {'SEL1':SEL1,
            'SEL2':SEL2,
            'EML1':EML1,
            'EML2':EML2}
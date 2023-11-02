print("My module is running")

def c2f():
    usertemp = (input("Enter the temp you want converted to degrees Fahrenheit: "))
    temp = float(usertemp)
    print(type(temp))
    return((temp * 1.8) + 32)

def f2c(value):
    return (value - 32) / 1.8

def dd(latdegree, latminute, latsecond, latdirection , londegree, lonminute, lonsecond, londirection):
    latdd = latdirection * (latdegree + (latminute + latsecond/60.0)/60.0)
    londd = londirection * (londegree + (lonminute + lonsecond/60.0)/60.0)
    return latdd, londd

def mph2kph(mph):
    """
    Convert miles per hour (mph) to kilometers per hour (km/h).

    Args:
        mph (float): Miles per hour.

    Returns:
        float: Kilometers per hour.
    """
    return mph * 1.60934

def kph2mph(kph):
    """
    Convert kilometers per hour (km/h) to miles per hour (mph).

    Args:
        kmph (float): Kilometers per hour.

    Returns:
        float: Miles per hour.
    """
    return kph / 1.60934

def lbs2_kg(pounds):
    """
    Convert pounds to kilograms.

    Args:
        pounds (float): Pounds.

    Returns:
        float: Kilograms.
    """
    return pounds * 0.453592

def kg2lbs(kilograms):
    """
    Convert kilograms to pounds.

    Args:
        kilograms (float): Kilograms.

    Returns:
        float: Pounds.
    """
    return kilograms / 0.453592

def ft2m(feet):
    """
    Convert feet to meters.

    Args:
        feet (float): Feet.

    Returns:
        float: Meters.
    """
    return feet * 0.3048

def m2ft(meters):
    """
    Convert meters to feet.

    Args:
        meters (float): Meters.

    Returns:
        float: Feet.
    """
    return meters / 0.3048

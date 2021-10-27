import math;

gsUnits = "?kMGTPEZY";
def fsBytesToHumanReadableString(uBytes, bShortNotation = False):
  if uBytes < 1000:
    if bShortNotation:
      return "%d B" % uBytes;
    return "%d byte%s" % (uBytes, "s" if uBytes != 1 else "");
  uMagnitude = int(math.log(max(1, uBytes), 1000));
  # We want to convert 999499 to 999 kB and 999500 to 1.00 MB
  # So we round the number given the magnitude and increase the magnitude by
  # one if the rounded number is 1000 or larger:
  nRounded = round(float(uBytes) / (1000 ** uMagnitude));
  if nRounded >= 1000:
    uMagnitude += 1;
  sUnit = gsUnits[uMagnitude] + "B" if uMagnitude else "B" if bShortNotation else "byte%s" % ("s" if uBytes != 1 else "");
  nUnits = float(uBytes) / (1000 ** uMagnitude);
  if uMagnitude == 0:
    uFloatingPointDigits = 0;
  else:
    uUnitsMagnitude = int(math.log(nUnits, 10));
    uFloatingPointDigits = max(0, 2 - uUnitsMagnitude);
  return "%%.%df %%s" % uFloatingPointDigits % (nUnits, sUnit);

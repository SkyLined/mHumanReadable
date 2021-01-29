import math;

gsUnits = ["?kMGTPEZY"];
def fsBytesToHumanReadableString(uBytes):
  uMagnitude = int(math.log(max(1, uBytes), 1000));
  sUnit = gasUnits[uMagnitude] + "B" if uMagnitude else "byte%s" % ("s" if uBytes != 1 else "");
  nUnits = float(uBytes) / (1000 ** uMagnitude);
  if uBytes < 1000:
    uFloatingPointDigits = 0;
  else:
    uUnitsMagnitude = int(math.log(nUnits, 10));
    uFloatingPointDigits = max(0, 2 - uUnitsMagnitude);
  return "%%.%df %%s" % uFloatingPointDigits % (nUnits, sUnit);

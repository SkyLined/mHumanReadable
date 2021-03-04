def fsArrayToHumanReadableString(asValues, sJoiner = "and"):
  if len(asValues) == 1:
    return asValues[0];
  return (
    ", ".join(asValues[:-1])
    + (len(asValues) > 2 and "," or "")
    + " " + sJoiner + " " + asValues[-1]
  );


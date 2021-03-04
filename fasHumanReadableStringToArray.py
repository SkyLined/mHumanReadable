import re;

rComma = re.compile(r"\s*,\s*");

def fasHumanReadableStringToArray(sValues, sJoiner = "and"):# "One"      || "One and Two"     || "One, Two, and Three"
  rJoiner = re.compile(r"(?:^|\s+)%s\s+" % re.escape(sJoiner));
  asValues = rComma.split(sValues);                         # ["One"]    || ["One and Two"]   || ["One", "Two", "and Three"]
  asLastValues = rJoiner.split(asValues.pop());             # [] ["One"] || [] ["One", "Two"] || ["One", "Two"] ["", "Three"]
  if asLastValues[0] == "": asLastValues.pop(0);            # [] ["One"] || [] ["One", "Two"] || ["One", "Two"] ["Three"]
  return asValues + asLastValues;                           # ["One"]    || ["One", "Two"]    ||  ["One", "Two", "Three"]

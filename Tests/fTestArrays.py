from mHumanReadable import fsArrayToHumanReadableString, fasHumanReadableStringToArray;

def fTestArrays():
  for (asInput, sJoiner, sExpectedOutput) in (
    (["One"],                         "and", "One"),
    (["One", "Two"],                  "and", "One and Two"),
    (["One", "Two", "Three"],         "and", "One, Two, and Three"),
    (["One", "Two", "Three", "Four"], "and", "One, Two, Three, and Four"),
    (["One"],                         "or", "One"),
    (["One", "Two"],                  "or", "One or Two"),
    (["One", "Two", "Three"],         "or", "One, Two, or Three"),
    (["One", "Two", "Three", "Four"], "or", "One, Two, Three, or Four"),
  ):
    sOutput = fsArrayToHumanReadableString(asInput, sJoiner);
    assert sExpectedOutput == sOutput, \
        "fsArrayToHumanReadableString(%s) != %s (but %s)" % (repr(asInput), repr(sExpectedOutput), repr(sOutput));
    asOutput = fasHumanReadableStringToArray(sOutput, sJoiner);
    assert asInput == asOutput, \
        "fasHumanReadableStringToArray(%s) != %s  (but %s)" % (repr(sOutput), repr(asInput), repr(asOutput));

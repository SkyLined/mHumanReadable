from mHumanReadable import fsBytesToHumanReadableString;

def fTestBytes():
  def fCheck(uBytes, sExpectedOutput):
    sOutput = fsBytesToHumanReadableString(uBytes);
    assert sExpectedOutput == sOutput, \
        "fsBytesToHumanReadableString(%s) != %s (but %s)" % (repr(uBytes), repr(sExpectedOutput), repr(sOutput));
  
  fCheck(1,                               "1 byte");
  fCheck(2,                               "2 bytes");
  fCheck(999,                             "999 bytes");
  fCheck(1000,                            "1.00 kB");
  fCheck(999499,                          "999 kB");
  fCheck(999500,                          "1.00 MB");
  fCheck(1000*1000,                       "1.00 MB");
  fCheck(999499999,                       "999 MB");
  fCheck(999500000,                       "1.00 GB");
  fCheck(1000*1000*1000,                  "1.00 GB");
  fCheck(12345,                           "12.3 kB");

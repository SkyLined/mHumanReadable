A number of function that return common types of data into a human readable
string, or vice versa. Currently implements:

fsBytesToHumanReadableString(uBytes)
====================================
Converts a size in bytes into a string such as "123Mb" or "1.5Gb".

Examples:
```
fsBytesToHumanReadableString(1) == "1 byte"
fsBytesToHumanReadableString(2) == "2 bytes"
fsBytesToHumanReadableString(999) == "999 bytes"
fsBytesToHumanReadableString(1000) == "1.00 kB"
fsBytesToHumanReadableString(1000*1000) == "1.00 MB"
fsBytesToHumanReadableString(12345) == "12.3kB"
```

fsArrayToHumanReadableString(asValues, sJoiner = "and")
=======================================================
Converts an array of strings into a comma separated list, such as "a, b, and c".
The optional joiner (default = "and") is used to indicate the way the elements
are combined by the list.

Examples:
```
fsArrayToHumanReadableString(["one"]) == "one"
fsArrayToHumanReadableString(["one", "two"]) == "one and two"
fsArrayToHumanReadableString(["one", "two", "three"]) == "one, two, and three"
fsArrayToHumanReadableString(["A", "B", "C"], "or") == "A, B, or C"
fsArrayToHumanReadableString(["true", "false"], "or") == "true or false"
```

fasHumanReadableStringToArray(sValue, sJoiner = "and")
======================================================
Converts a string containing a comma separated list into a list of strings. The
optional jioned (default = "and") is used to to indicate the way the elements
are combined by the string.

Examples:
```
fasHumanReadableStringToArray("one") == ["one"];
fasHumanReadableStringToArray("one and two") == ["one", "two"];
fasHumanReadableStringToArray("one, two, and three") == ["one", "two", "three"];
fasHumanReadableStringToArray("A, B, or C", "or") == ["A", "B", "C"];
fasHumanReadableStringToArray("true or false", "or") == ["true", "false"];
```

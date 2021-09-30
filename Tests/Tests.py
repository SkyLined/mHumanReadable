import os, sys;
sModulePath = os.path.dirname(__file__);
sys.path = [sModulePath] + [sPath for sPath in sys.path if sPath.lower() != sModulePath.lower()];

from fTestDependencies import fTestDependencies;
fTestDependencies();

from fTestArrays import fTestArrays;
from fTestBytes import fTestBytes;

fTestArrays();
fTestBytes();

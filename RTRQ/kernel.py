import sys
sys.path.append('./')
from RTRQ.Extension.KernelDefault import *

def kernel_generate():
	import ServiceApp.service_Build.main
	import ServiceApp.service_CLI.main
	import ServiceApp.service_cmHardware.main
	import ServiceApp.service_Hextor.main
	import ServiceApp.service_manageBoot.main
	import ServiceApp.service_manageFrame.main
	import ServiceApp.service_Serial.main

import tweepy as tp
import time
import os
from datetime import datetime

t = time.localtime()
now = time.strftime("%I:%M", t)


#0sYeNKrgELrbQOpKx55wsbMvv
#HovGWG2x5d3Qlse79AHiV40h2mENPBhAKtunwYz1MrqjT9DBrK
#AAAAAAAAAAAAAAAAAAAAAEmyEgEAAAAAAdairUTOqlvCwgOhunl%2FRgYteJ4%3DttLgVuRQpTRYD5mokSbId43ZjKexaBJ1zVcm3EaTMK02oBHdcC

auth = tp.OAuthHandler("jmT1EN6h5pRGx2pMkksi4UU1U", "sCNNI2TDT76t7g4Zajmg2qLaAr6MvPn6i3ZeQiASQEHADkeyuk")
auth.set_access_token("1265104472780439557-wKlObONBvB1fdJ7pVXO4bdTc9InJSj", "LtNItaXxnJRVHv6sebAfpwhNiSCzy0qUDZXeXVQvOXkVm")
api = tp.API(auth)

while(True):
	t = time.localtime()
	now = time.strftime("%I:%M", t)

	if now == "09:23":
		update = "Yes. Time:" + now
		api.update_status(update)

	if now != "09:23":
		update = "No. Time = " + now
		api.update_status(update)

	time.sleep(60)

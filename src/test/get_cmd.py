import subprocess

#mod EMAIL UUID API_ADDRESS API_PORT 
#INBOUND_TAG LEVEL ALTERID
#message = os.popen("""/usr/bin/v2ray/v2ctl api --server=127.0.0.1:10085 StatsService.GetStats 'name: "user>>>123@gmail.com>>>traffic>>>downlink" reset: false'""").readlines()
#message = os.popen("""./v2rayapi add 123@email.com fdea10a8-1382-11ea-8d71-362b9e155667 127.0.0.1 10085 ahhhh 1 10""").readlines()
command = """./v2rayapi del 123@email.com fdea10a8-1382-11ea-8d71-362b9e155667 127.0.0.1 10085 ahhhh 1 10"""



back = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
for x in back:
	print(x.decode())


import requests
import colorama
colorama.init()
def startmassage():
    print("#"+"*"*77+"#")
    print("| Script Name :                       Dirbrute                                |")
    print("| About Me    : [ Mohammad Abd Almoenam ] -Web Devloper- And -Ethical Hacker- |")
    print("| Facebook    :       ( https://www.facebook.com/alqnasfox )                  |")
    print("| Youtube     :  (https://www.youtube.com/channel/UCFEmcI1LJKYXgD5_PQ4rm-Q)   |")
    print("| My Website  :         ( https://alqnasfox.blogspot.com )                    |")
    print("#"+"*"*77+"#")
    print("\n")
startmassage()
# define colors
GREEN = colorama.Fore.GREEN
RED   = colorama.Fore.RED


try:
	url 		  = input("[*] Insert Url To Bruteforce : ")
	wordlist_path = str(input("[*] Insert Wrdlist Path : "))
	cheakvalue    = str(input("[*] Cheak Value example [page not found] Leave Empty For Default [404] : "))
	startpoint    = int(input("[*] Insert Start Point : "))
	reports_path  = "reports/"
	report_file_name = url.split("/")[2]+".txt"
	wordlist = open(wordlist_path,"r")
	mk_report = open(reports_path+report_file_name,"a")
except KeyboardInterrupt :
	exit("Good By ...(-_-)")
except :
	exit("Cheak Your Inputs Make Sure From wordlist path")

def brute(full_url):
	try:
		x = requests.get(full_url)
		return x
	except:
		pass

res_count = 0
counter = 0
try:
	for word in wordlist:
		counter +=1
		if counter >= startpoint :
			word = word.split()[0]
			full_url = url+"/"+word
			result = brute(full_url)
			status_code = result.status_code
			if len(cheakvalue) < 3:
				if result.status_code != 200:
					print(f"{RED}[-] [{counter}] {full_url } --> {status_code}")
				else:
					res_count += 1
					mk_report.write(f"[{res_count}] {full_url} \n")
					print(f"{GREEN}[+] [{counter}] Found Dir --> {full_url} status_code[{status_code}]")
			else:
				if cheakvalue in result.text:
					print(f"{RED}[-] [{counter}] {full_url } --> {status_code}")
				else:
					res_count += 1
					mk_report.write(f"[{res_count}] {full_url} \n")
					print(f"{GREEN}[+] [{counter}] Found Dir --> {full_url} status_code[{status_code}]")

	wordlist.close()
	mk_report.close()
	print(f"{GREEN}[info] Result Was Found [{res_count}] Saved To reports < -- > {report_file_name}")
except KeyboardInterrupt:
	print('Exiting ...')
	print(f"{GREEN}[info] Result Was Found [{res_count}] Saved To reports < -- > {report_file_name}")
	exit(0)
except:
	exit(0)
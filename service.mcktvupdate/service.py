import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys
import urllib2, urllib

path = xbmc.translatePath('special://home/addons/service.mcktvupdate')

installed = xbmc.translatePath("special://home/installedversion.txt")
latest = xbmc.translatePath("special://home/addons/service.mcktvupdateupdate/latestversion.txt")

def path():
	if not os.path.exists(path):
		os.mkdir(path)

url = 'http://mcktv.co.uk/mcktvupdate/latest_version.txt'
urllib.urlretrieve(url, latest)


file_i = open(installed)
file_i.close()

file_l = open(latest, 'r')
checksum_latest = file_l.read()
file_l.close()

def check(checksum):
	datafile = file(installed)
	updated = False
	for line in datafile:
		if checksum in line:
			updated = True
			break
	return updated

def wizard():
	choice = xbmcgui.Dialog().yesno('MckTV Updater', 'Update available for MckTV', 'Select OK to start updating', nolabel='Cancel',yeslabel='OK')
	if choice == 0:
		return
	elif choice == 1:
		#xbmc.executebuiltin("RunAddon(plugin.program.kodikingbuildwizard)")
		xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.mcktv/?url=https%3A%2F%2Farchive.org%2Fdownload%2Fmcktvup2.17%2Fmcktvup2.17.zip&amp;mode=1&amp;name=Install+Update&amp;iconimage=https%3A%2F%2Farchive.org%2Fdownload%2Fmcktvlogo%2FMckTVlogo.png&amp;fanart=https%3A%2F%2Farchive.org%2Fdownload%2Fstartup_201512%2Fstartup.jpg&amp;description=MckTV+Update)')
		file_i = open(installed, "w")
		file_i.write(checksum_latest)
		file_i.close()
		file_i = open(installed)
		checksum_updated = file_i.read()
		file_i.close()

if check(checksum_latest):
	xbmc.sleep(1000)
else:
	wizard()

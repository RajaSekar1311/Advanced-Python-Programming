myCSVFileName = 'VideoSharingTraffic.csv'
backupFileName = myCSVFileName.split('.csv')
fileExists = os.path.isfile(myCSVFileName)
if fileExists:
	#Taking the backup of the previously generated video sharing traffic file
	currentTimeStamp = datetime.datetime.now()
	backupFileName = backupFileName[0]+'_Backup_'+currentTimeStamp.strftime('%d-%m-%Y_%H%M%S')+'.csv'
	print('Taking the backup of existing Video Sharing Traffic CSV file...')
	print('Backup is taken in a new file:  '+backupFileName)
	os.rename(myCSVFileName,backupFileName)
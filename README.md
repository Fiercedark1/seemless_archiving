I left you the public key to the search to gain access. These are my scripts to move files over from one directory to another. The first tar's and moves files from one directory to an archiving directory for files 3 hours or older on an hourly bases. The second checks the archiving directory for tar files older then 3 hours on an hourly bases. 

I used "*/1 * * * *" /path/to/script/ within crontab to establish a quick test.
Then after success I changed crontab to "0 * * * *" /path/to/script so to have it run on the hour every hour.

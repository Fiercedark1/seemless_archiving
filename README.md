# Seamless File Movement
Description: The repo contains python 2.7 scripts that move files that are 3 hours or older. There are two directories here the 3hr_limit/ which holds the original files and the tmp_arch/ directory that acts as our tar archive.
The first script (time_limit.py) compresses and moves files from 3hr_limit/ that are 3 hours or older to the tmp_arch/. The second script (untar_revive.py) is a revive script that decompresses the tar files from tmp_arch/ and moves them back to 3hr_limit/.

Its a simple example of file movement based on file age with the use of crontab to manage scheduling.

## Installation
`Linux`

1. Open directory you are going to be working in and `git clone git@github.com:Fiercedark1/seemless_archiving.git`

2. Once the clone is complete run the `./install.sh` script as root

3. Your done! Now any file you put in 3hr_limit/ will be managed by the scripts

## Usage
If you would like to make modification to either the script or crontab's scheduling here are some tips.

- Age of file
Look for the variable `diff_hours`. The math is based in seconds. Changes are to be made to diff_hours = now - <insert time>
  Here are a few examples:
  - 1 hour  = 3600 seconds
  - 1 day   = 86400 seconds
  - 1 week  = 604800 seconds
  - 1 month = 2419200 seconds
  - 7 Days  = 7 * 86400
  - 3 Hours = 3 * 3600
- Crontab
As you may have noticed the install script (./install.sh) installed crontab if you haven't done so already.
Go ahead and enter the command `crontab -e`
It will open up a text editor and it is in here line per line that you enter the scheduling.
The syntax for crontab is ` * * * * * /path/to/script`
Each * meaning a different area of time. I've added two for you already. Just comment one and uncomment the other.

              | field   |   meaning    |   allowed values |
              |---------|--------------|------------------|
              |    1    |    minute    |       0-59       |
              |    2    |    hour      |       0-23       |
              |    3    | day of month |        1-31      |
              |    4    |    month     |        1-12      |
              |    5    |  day of week |   0-7 (0 | 7=Sun)|

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
  This was a project that was asked of me when I was applying to Harvard University. I thought this seems like something that a lot of people would find useful so I changed a few things and now its here. Enjoy!

## Name Drops
 Thanks to http://alvinalexander.com/linux/unix-linux-crontab-every-minute-hour-day-syntax for the crontab documentation.
]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>

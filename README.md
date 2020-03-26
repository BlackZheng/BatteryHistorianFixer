##Battery Historian Fixer
---
A python script that make your bugreport from Android Q to be accepted by [Battery Historian](https://github.com/google/battery-historian)

##Why you need it？
---
For some reasons, [bugreport from Android Q can't be parsed](https://github.com/google/battery-historian/issues/182) by Battery Historian and throw a error says `Could not parse aggregated battery stats.`
Batterian Historian Fixer help to work it out. 

##Usage
---
usage: python battery_historian_fixer.py <source_file_path> [-v]

* -v provides more details as it runs

##Note
---
* This script only receive `txt` file.
* For bugreport.zip, you need to unzip it and find the bugreport_xxxx.txt.
* The script will generate a new bugreport file named `<original_filename>_fixed.txt`. Then you  can give it to Battery Historian.

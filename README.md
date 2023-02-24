# Steam-Cyber-Forensics-

These files were created to assist in analysis and collection of Steam artifacts by conversion to XLSX format after listing files of interest. 

The first file to be used is **"FileLists.py"**. This script will read the default directory of a steam download :\Program Files (x86)\Steam and lists the files in an xlsx sheet. The sheet will be broken into three tabs containing VDF, JSON, and TXT files. To edit the directory that is searched if steam is installed in a different location change line #37 to the path of the install. The variable on line #35 contains a list of languages an other words to reduce the amount of files that are found that may not contain forensic relevance. Commenting line #35 or removing one of the languages or words will result in files being found containing the word removed out of the list.

The second file to be used is **"SteamContentParser.py"**. The files found in the first script will need to be moved into a folder named "SourceFiles" once in that folder the script will move through each file and add them to a tab based on VDF, JSON, or TXT file extension. To change the name of the folder edit line #170. This line contains "in os.walks('SourceFiles')" changing the name SourceFiles will result in a search for a different folder.

**Libraries needed to run the files**

* import os (default to python) <br>
* import json (default to python) <br>
* import xlsxwriter (pip install xlsxwriter) <br>
* import openpyxl (pip install openpyxl) <br>

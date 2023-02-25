This file contains instructions to edit the file **SteamContentParser.py**

This file is primarly made of code blocks that can be added, removed, or modified to change data the script parses. 
Below are the blocks that need to be changed; I will be using the example of how to add a database file or .db extension 
to the content parsing.

**Block 1**
```
#Creating worksheet for text files
txt_ws = workbook.add_worksheet('Txt Files')
#Labeling A1 for text files and formatting cell
txt_ws.write(0,0,'File Name',cell_format)
#Setting width of A1 to length of header name + 1 (File Name is 9 characters + 1 = 10)
txt_ws.set_column(0,0,10)
#Labeling A2 for text files and formatting cell
txt_ws.write(0,1,'Line',cell_format)
#Setting width of A2 to len(header) + 1
txt_ws.set_column(1,1,5)
#Labeling A3 for text files and formatting cell
txt_ws.write(0,2,'Content',cell_format)
#Setting width of A3 len(header) + 1
txt_ws.set_column(2,2,8)
```
**<div align="center">Modifying Block 1</div>**

This block is located on lines 15-27, you can copy this whole block and, after moving line 29 down to line 31, paste this block
on line 29. With the block in place change *txt_ws* to *db_ws* in every instance

<div align="center">Example:</div> <br>

```
#Creating worksheet for database files
db_ws = workbook.add_worksheet('Txt Files')
#Labeling A1 for database files and formatting cell
db_ws.write(0,0,'File Name',cell_format)
#Setting width of A1 to length of header name + 1 (File Name is 9 characters + 1 = 10)
db_ws.set_column(0,0,10)
#Labeling A2 for database files and formatting cell
db_ws.write(0,1,'Line',cell_format)
#Setting width of A2 to len(header) + 1
db_ws.set_column(1,1,5)
#Labeling A3 for database files and formatting cell
db_ws.write(0,2,'Content',cell_format)
#Setting width of A3 len(header) + 1
db_ws.set_column(2,2,8)
```
**Block 2**
```
#Tracking line number in JSON tab
json_line_constant = 1
#Tracking JSON header size
json_header = 10
#Tracking line number in Text tab
txt_line_constant = 1
#Tracking Txt header size
txt_header = 10
#Tracking line number in VDF tab
vdf_line_constant = 1
#Tracking VDF header size
vdf_header = 10
```
**<div align="center">Modifying Block 2</div>**

After the line vdf_header = 10 add the same comments that are seen but including Database as the file you are tracking.
Modify the lines to read db_line_constant = 1 and db_header = 10

<div align="center">Example:</div> <br>

```
#Tracking line number in VDF tab
vdf_line_constant = 1
#Tracking VDF header size
db_reader = 10
#Tracking line number in DB tab
db_line_constant = 1
#Tracking db header size
db_header = 10
```
**Block 3**
```
def json_parser(file_path,filename):
    #Opening the file as a binary object
    with open(file_path,'rb') as my_file:
        #Reading in the JSON data
        json_data = json.load(my_file)
        #Declaring variables as global
        global json_line_constant
        global json_header

        #Tracking line number in each file
        line_count = 1

        for each_line in json_data:
            #Adding the filename to the appropriate line and column
            json_ws.write(json_line_constant,0,filename)
            #Adding line number from file
            json_ws.write(json_line_constant,1,line_count)
            #Writing line data, tries to decode the binary data, if unable to decode, it writes the binary in the except
            try:
                json_ws.write(json_line_constant,2,str(each_line.decode('utf-8')).strip())
            except:
                json_ws.write(json_line_constant,2,str(each_line).strip())

            #Checking for size of the filename to readjust header column
            if len(filename) > json_header:
                json_ws.set_column(0,0,len(filename))
                json_header = len(filename)

            #Moving to the next line
            json_line_constant += 1
            line_count += 1
```

**<div align="center">Modifying Block 3</div>**

This code will be copied and pasted to line 167 after moving the current line 167 is moved down to line 169.
Once the block is in place change the following

json_parser ➡️ db_parser <br>
json_data = json.load ➡️ db_parser = db.load <br>
global json_line_constant ➡️ global db_line_constant <br>
global json_header ➡️ global db_header <br>
json_ws.write(json_line_constant,0,filename) ➡️ db_ws.write(db_line_constant,0,filename) <br>
json_ws.write(json_line_constant,1,line_count) ➡️ db_ws.write(db_line_constant,1,line_count) <br>
json_ws.write(json_line_constant,2,str(each_line.decode('utf-8')).strip()) ➡️ db_ws.write(db_line_constant,2,str(each_line.decode('utf-8')).strip()) <br>
json_ws.write(json_line_constant,2,str(each_line).strip()) ➡️ db_ws.write(db_line_constant,2,str(each_line).strip()) <br>
if len(filename) > json_header: ➡️ if len(filename) > db_header: <br>
json_ws.set_column(0,0,len(filename)) ➡️ db_ws.set_column(0,0,len(filename)) <br>
json_header = len(filename) ➡️ db_header = len(filename) <br>
json_line_constant += 1 ➡️ db_header = len(filename) <br>

<div align="center">Example:</div> <br>

```
def db_parser(file_path,filename):
    #Opening the file as a binary object
    with open(file_path,'rb') as my_file:
        #Reading in the Database data
        db_data = json.load(my_file)
        #Declaring variables as global
        global db_line_constant
        global db_header

        #Tracking line number in each file
        line_count = 1

        for each_line in db_data:
            #Adding the filename to the appropriate line and column
            db_ws.write(db_line_constant,0,filename)
            #Adding line number from file
            db_ws.write(db_line_constant,1,line_count)
            #Writing line data, tries to decode the binary data, if unable to decode, it writes the binary in the except
            try:
                db_ws.write(db_line_constant,2,str(each_line.decode('utf-8')).strip())
            except:
                db_ws.write(json_line_constant,2,str(each_line).strip())

            #Checking for size of the filename to readjust header column
            if len(filename) > db_header:
                db_ws.set_column(0,0,len(filename))
                db_header = len(filename)

            #Moving to the next line
            db_line_constant += 1
            line_count += 1
```

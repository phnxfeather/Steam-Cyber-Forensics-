#Library to walk through directory structure
import os
#Writes to Excel files
#3rd party library, requires install through: pip install xlsxwriter
import xlsxwriter
#Required to use json library
import json

#Creating workbook
workbook = xlsxwriter.Workbook('steam_data.xlsx')
#Creating formating to add to header cell
cell_format = workbook.add_format({'bold':True})

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

#Creating worksheet for JSON files
json_ws = workbook.add_worksheet('JSON Files')
#Labeling A1 for json files and formatting cell
json_ws.write(0,0,'File Name',cell_format)
#Setting width of A1 to len(header) + 1
json_ws.set_column(0,0,10)
#Labeling A2 for json files and formatting cell
json_ws.write(0,1,'Line',cell_format)
#Setting width of A2 to len(header) + 1
json_ws.set_column(1,1,5)
#Labeling A3 for text files and formatting cell
json_ws.write(0,2,'Content',cell_format)
#Setting width of A3 to len(header) + 1
json_ws.set_column(2,2,8)

#Creating worksheet for VDF files
vdf_ws = workbook.add_worksheet('VDF Files')
#Labeling A1 for json files and formatting cell
vdf_ws.write(0,0,'File Name',cell_format)
#Setting width of A1 to len(header) + 1
vdf_ws.set_column(0,0,10)
#Labeling A2 for json files and formatting cell
vdf_ws.write(0,1,'Line',cell_format)
#Setting width of A2 to len(header) + 1
vdf_ws.set_column(1,1,5)
#Labeling A3 for text files and formatting cell
vdf_ws.write(0,2,'Content',cell_format)
#Setting width of A3 to len(header) + 1
vdf_ws.set_column(2,2,8)

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

#Parsing JSON file
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

#Parsing text files
def txt_parser(file_path,filename):
    #Opening text files as binary
    with open(file_path,'rb') as my_file:
        #Declaring variables as global
        global txt_line_constant
        global txt_header

        #Tracking line number in each file
        line_count = 1

        for each_line in my_file:
            #Adding the filename to the appropriate line and column
            txt_ws.write(txt_line_constant,0,filename)
            #Adding line number from file
            txt_ws.write(txt_line_constant,1,line_count)
            #Writing line data, tries to decode the binary data, if unable to decode, it writes the binary in the except
            try:
                txt_ws.write_string(txt_line_constant,2,str(each_line.decode('utf-8')).strip())
            except:
                txt_ws.write_string(txt_line_constant,2,str(each_line).strip())

            #Checking for size of the filename to readjust header column
            if len(filename) > txt_header:
                txt_ws.set_column(0,0,len(filename))
                txt_header = len(filename)
            
            #Moving to the next line
            txt_line_constant += 1
            line_count += 1

#Parsing VDF files
def vdf_parer(file_path,filename):
    #Opening VDF files as binary
    with open(file_path,'rb') as my_file:
        #Declaring variables as global
        global vdf_line_constant
        global vdf_header

        #Tracking line number in each file
        line_count = 1

        for each_line in my_file:
            #Adding the filename to the appropriate line and column
            vdf_ws.write(vdf_line_constant,0,filename)
            #Adding line number from file
            vdf_ws.write(vdf_line_constant,1,line_count)
            #Writing line data, tries to decode the binary data, if unable to decode, it writes the binary in the except
            try:
                vdf_ws.write_string(vdf_line_constant,2,str(each_line.decode('utf-8')).strip())
            except:
                vdf_ws.write_string(vdf_line_constant,2,str(each_line).strip())

            #Checking for size of the filename to readjust header column
            if len(filename) > vdf_header:
                vdf_ws.set_column(0,0,len(filename))
                vdf_header = len(filename)
            
            #Moving to the next line
            vdf_line_constant += 1
            line_count += 1

#Main function to walk through the folder structure looking for the files
def parser_builder():
    #Looks for a folder called 'Source Files' in the same directory as the Python script
    for dir_path, dir_names, filenames in os.walk('SourceFiles'):
        #Loops through all the files found
        for filename in filenames:
            #Creates path and filename variable
            file_path = os.path.join(dir_path, filename)

            #Checks if JSON file and passes it to the JSON parser
            if '.json' in file_path:
                json_parser(file_path,filename)
            #Checks if txt file and passes it to the txt parser
            elif '.txt' in file_path:
                txt_parser(file_path,filename)
            #Checks if VDF file and passes it to the VDF parser
            elif '.vdf' in file_path:
                vdf_parer(file_path,filename)
            #Checks for any other file
            else:
                print('Found an unknown file.')

#Closes the Excel workbook
def close_spreadsheet():
    workbook.close()

#Starts the script running
if __name__ == '__main__':
    parser_builder()
    close_spreadsheet()

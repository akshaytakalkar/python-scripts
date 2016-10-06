
import sys
def replace_line(location,content,tomod):
# with is like your try .. finally block in this case
    with open( location, 'r') as file:
    # read a list of lines into data
        data = file.readlines()

    cnt=0
# now change the line by keyword, note that you have to add a newline
    for lin in data:
        cnt=cnt+1
        print cnt    
        if tomod in lin:
	    data[cnt-1]= content
# and write everything back
    with open(location, 'w') as file:
        file.writelines( data )
    file.close()
loc='/FILE/LOCATION'
tomod="ATTRIBUTE TO IDENTYFY"
content="CONTENT TO ADD"
replace_line(loc,content,tomod)

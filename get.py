import requests
from bs4 import BeautifulSoup as BS

"""
index 0 for title, 
1 for first team name, 
2 for first team score, 
3 for second team name , 
4 for second team score ,
5 for status report
"""

def get_source():
    source = requests.get("http://www.cricbuzz.com")
    soup = BS(source.content, "lxml")
    #print source.content
    #print "\n\n\n"
    #print(unicode(soup.prettify()).encode('utf-8'))
    useful_data = soup.find_all("div", "cb-mtch-blk")
    matches = []
    titles = []
    for x in useful_data:
        
        cur_title = x.find("a")['title']
        if cur_title in titles:
            continue
        
        matches.append([0, 1, 2, 3, 4, 5])
        
        titles.append( cur_title )
        matches[-1][0] = cur_title
        
        completed = x.find(class_="cb-text-complete")
        on_going = x.find(class_="cb-text-live")                              
        to_come = x.find(class_="cb-text-preview")
        if completed is not None:
            matches[-1][5] = completed.string
            temp = x.find(class_="cb-hmscg-bat-txt")
            matches[-1][1:3] = [temp2.string for temp2 in temp.find_all(class_="cb-ovr-flo")]
            temp = x.find(class_="cb-hmscg-bwl-txt")
            matches[-1][3:5] = [temp2.string for temp2 in temp.find_all(class_="cb-ovr-flo")]
            
        elif to_come is not None:
            matches[-1][5] = "Not yet started"
            matches[-1][1],matches[-1][3] = [temp2.string for temp2 in x.find_all(class_="cb-hmscg-bat-txt")]
            matches[-1][2],matches[-1][4] = None, None
        else:
            matches[-1][5] = on_going.string
            temp = x.find(class_="cb-hmscg-bat-txt")
            matches[-1][1:3] = [temp2.string for temp2 in temp.find_all(class_="cb-ovr-flo")]
            temp = x.find(class_="cb-hmscg-bwl-txt")
            matches[-1][3:5] = [temp2.string for temp2 in temp.find_all(class_="cb-ovr-flo")]
    """
    for x in matches:    
        print x
    """
         
get_source()
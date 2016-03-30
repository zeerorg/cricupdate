import get
from gi.repository import Gtk
import time
from threading import Thread

class MainWindow(Gtk.Window):
    
    def __init__(self, title):
        Gtk.Window.__init__(self, title=title)
        self.list_store_data()
        self.thr = Thread(target = self.update)
        self.thr.start()
        self.add(self.tree)
        self.connect("delete-event",Gtk.main_quit)
        
    def update(self):
        while not stopit:
            time.sleep(5)
            arr = get.get_source()
            for n_x,x in enumerate(arr):
                for y in range(6):
                    self.store[n_x][y] = x[y]
	    self.show_all()
            #print arr
                
    def list_store_data(self):
        self.store = Gtk.ListStore(str, str, str, str, str, str)
        storearr = []
        arr = get.get_source()
        self.tree = Gtk.TreeView(self.store)
        for x in arr:
            storearr.append(self.store.append(list(x)))
            
        
        top_title = ['Match', 'Team 1', 'Team 1 score', 'Team 2', 'Team 2 score', 'Result']
        render = []
        column = []
        for x in range(6):
            render.append(Gtk.CellRendererText())
            
        for x in range(6):
            column.append(Gtk.TreeViewColumn(top_title[x], render[x], text=x))
            
        for x in range(6):
            self.tree.append_column(column[x])
            
        #print arr
stopit = False
window = MainWindow("Cric Update")
window.show_all()
Gtk.main()
stopit = True

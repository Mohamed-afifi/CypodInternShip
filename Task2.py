import math

lis=[]

#abstract class
class box:
    
    def add():
        pass

    def empty():
        pass
        
    def count():
        pass    
    



class item:
   
    def __init__(self,name="Name",value=0):
        self.name=name
        self.value=value
    
        


        
    

#dont use static class methods
#store items inside instance of class not in global variables
#listbox  "has a " relationship with "item"
#store item objects as list

class ListBox(box,list):
        
        def __init__(self):
            self.lis = []
        
        def add(self,i):
            check=isinstance(i,item)
            if(check):
                self.lis.append(i)
            else:
                raise Exception("Sorry, wrong values. not of type item")
            
        def empty(self):
            newlist=[]
            newlist=self.lis.copy()
            self.lis.clear()
            return newlist
            
        def count(self):
            return(len(self.lis))
               

             
        
class DictBox(box,list):  
  
        def __init__(self):
            self.list2=[]
            self.mydict={}

        def add(self,i):
            check2=isinstance(i,item)
            if(check2):
               self.mydict[i.name]=i
            else:
                raise Exception("Sorry, wrong  values. not of type item")

        def empty(self):
            return list(self.mydict.values())
            self.mydict.clear()
        def count(self):
            return(len(self.mydict))

    
        





box1 =ListBox()
box2 =ListBox()
box3 =DictBox()

mylist1=[("Mouse",20),("keyboard",10),("Ram",15),("Screen",11),("HardDisk",12), ("Apple",5), ("Orange",7), ("Dates",20),("Banana",4),("Cherry",3)
        ,("Laptop",25), ("Watch",13), ("Table",2), ("Bag",6), ("Comb",1),
        ("Box",3),("Switch",15), ("Mobile",122), ("Earphones",25), ("Window",29)
         ] #the 20 item
mylist2=[("Songs",50), ("Games",25), ("Applications",100), 
         ("Settings", 30), ("Siri",70),("Wallpaper",20), 
         ("Software",90), ("Buttons",100), ("Taps",78) ]#the 9 items


MyDict={"Chair":70, "Sofa":80, "Desk":40, "curtains": 88, "Mats": 75} #the 5 item dict




for i in mylist1:
     item1=item(i[0],i[1])
     box1.add(item1)



for j in mylist2:
   item2=item(j[0],j[1])
   box2.add(item2)


for x in MyDict:
     tp=(x,MyDict[x])
     item3=item(tp[0],tp[1])
     box3.add(item3)





def repack(*args):
    RangeBoxes=0

    Listt=[]

    for argument in args:
        RangeBoxes+=argument.count()

    for itemList in args:
        items = itemList.empty()
        for i in items:
            Listt.append(i)


    print("The number of collected items is : ",RangeBoxes,"\n")
    
    Count_of_Boxes=(len(args))

    print("The number of boxes passed is : ",Count_of_Boxes,"\n")
   
    Desired=int(RangeBoxes/Count_of_Boxes)
    Desired2=int(Desired*2)
    boxx1=ListBox()
    boxx2=ListBox()
    boxx3=ListBox()
    temp1=Listt[0:Desired]
    temp2=Listt[Desired:Desired2]
    temp3=Listt[Desired2:RangeBoxes]

    for i in temp1:
        boxx1.add(i)
    for j in temp2:
        boxx2.add(j)
    for k in temp3:
        boxx3.add(k)
    print("The boxes after distribution will be : \n")
    print("The first box has :",boxx1.count())
    print("The second box has :",boxx2.count())
    print("The third box has :",boxx3.count())


    
    
    
    


    





  
      

repack(box1, box2, box3)

        
    
        






#item1 =  item(name, value)



#box1.add(item)

#item2 =  item(name, value)

#box2 =  DictBox()



#box2.add(item2)
    
#box
#listbox // dictbox


#box has items


#item has 2 properties
from re import search
from tabulate import *

class Voucher:
    def __init__(self,tdyDate,cust) -> None:
        self.date=tdyDate
        self.cust=cust
        self.lineList=[]
        self.price=self.calTotal()

    def addLine(self,line):
        self.lineList.append(line)
        self.price=self.calTotal()

    def calTotal(self):
        sum=0
        for line in self.lineList:
            sum+=line.subtotal
        return sum

class Customer:
    def __init__(self,name,phone,address) -> None:
        self.custName=name
        self.phone=phone
        self.address=address

class Line:
    def __init__(self,number,item,amount) -> None:
        self.number=number
        self.item=item
        self.amount=amount
        self.subtotal=self.item.itemPrice*self.amount

class Item:
    def __init__(self,item,itemPrice) -> None:
        self.item=item
        self.itemPrice=itemPrice

class ItemCreate:
    def __init__(self) -> None:
        self.itemList=[]
        self.createItem("Book",350)
        self.createItem("Pen",200)
        self.createItem("Pencil",100)
        self.createItem("Ruler",150)
        self.createItem("Correction Pen",1350)
        self.createItem("Eraser",250)
        self.createItem("Pencil Case",3500)

    def createItem(self,item,itemPrice):
        obj=Item(item,itemPrice)
        self.itemList.append(obj)
    
    def showItem(self):
        columns = ("Items","Item Price")
        infoList = []
        tList=[]
        for items in self.itemList:
            tList.append(items.item)
            tList.append(items.itemPrice)
            infoList.append(tList)
            print(tabulate(infoList,headers=columns))


    def getItemPrice(self,item):
        for i in self.itemList:
            if item==i.item:
                fees=i.itemPrice
        return fees

    def getItemObj(self,item):
        obj=None
        for i in self.itemList:
            if item==i.item.lower():
                obj=i
        return obj

import datetime
class CoCo:

    def __init__(self) -> None:
        self.voucherList=[]
        self.items=ItemCreate()
        #self.fillItems()

    """ def fillItems(self):
        x=""
        while x!= "a":
            x = input("Would you like to add an item? If so, type yes, if not type a ").lower()  
            if x == "a":
                break
            self.items.createItem(input("Please enter item name").lower(),int(input("Please enter item price"))) """

    def makeOrder(self):
        lineNo=0
        today=datetime.date.today()
        name= input("Welcome customer!Please enter your name! ").lower()
        phone=input("Please also enter you phone number! ")
        address=input("Please enter address")
        cust=Customer(name,phone,address)
        voucherObj=Voucher(today,cust)
        y="a"
        while y != "-999":
            y= input("What do you want to buy? If you no longer want to buy, type -999 ").lower()
            itemObj=self.items.getItemObj(y)
            if itemObj!=None:
                qty=int(input("Please enter quantity"))
                lineNo+=1
                lineObj=Line(lineNo,itemObj,qty)
                voucherObj.addLine(lineObj)
            else:
                print("Your item is out of stock!!! Please order later")
        self.voucherList.append(voucherObj)

    def showVoucher(self,custName):
        index=-1
        for i in range(len(self.voucherList)):
            cust=self.voucherList[i].cust
            if custName.lower()==cust.custName.lower():
                index=i
                break
        
        if index!=-1:
            voucher=self.voucherList[index]
            column=["No","Item Name","Item Price","Qty","Sub Total"]
            print("Date:",str(voucher.date.day)+"/"+str(voucher.date.month)+"/"+str(voucher.date.year))
            print("Customer Name:",voucher.cust.custName)
            twoD=[]
            for line in voucher.lineList:
                temp=[]
                temp.append(line.number)
                temp.append(line.item.item)
                temp.append(line.item.itemPrice)
                temp.append(line.amount)
                temp.append(line.subtotal)
                twoD.append(temp)
            print(tabulate(twoD,headers=column))
            print("Voucher Total:",voucher.price)

        else:
            print("Your name is invalid!! Please confirm your name.")

    def cancelOrder(self):
        dateObj,custName=self.getInfoToCancel()
        self.cancelVoucher(dateObj,custName)

    def getInfoToCancel(self):
        date=input("Please enter date in form dd/mm/yyyy")
        dateList=date.split("/")
        custName=input("Please enter customer name")
        dateObj=datetime.date(int(dateList[2]),int(dateList[1]),int(dateList[0]))
        return dateObj,custName

    def cancelVoucher(self,dateObj,custName):
        for voucher in self.voucherList:
            if dateObj==voucher.date and custName.lower()==voucher.cust.custName.lower():
                self.voucherList.remove(voucher)
                print("Voucher has been successfully canceled!!!")

    def calTodaySale(self):
        sum=0
        for voucher in self.voucherList:
            sum+=voucher.price
        return sum
    








        

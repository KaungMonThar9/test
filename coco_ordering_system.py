from ordering_system import*
def main():
    coco=CoCo()
    userOption=getUserOption()
    while userOption!=5:
        if userOption==1:
            coco.makeOrder()
        elif userOption==2:
            custName=input("Please enter customer name to search voucher")
            coco.showVoucher(custName)
        elif userOption==3:
            coco.cancelOrder()
        elif userOption==4:
            print("Today Total Sale:",coco.calTodaySale())
        userOption=getUserOption()
    print("Thanks for using my app ^_^")


def getUserOption():
    userMessage="Choose your option:\n\
    1:make order\n\
    2:show voucher\n\
    3:cancel order\n\
    4:calculate today Sale\n\
    5:exit"
    return int(input(userMessage))

main()
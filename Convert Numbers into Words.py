"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,such as 1 will be 
One, 2 will be two and 538 will be Five Hundred and Thirty Eight. This is how it would look like
"""
def main():
    andx,summation="and",0
    y={}
    y={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",1000:"Onethousand",andx:"and"}
    for i in range(1,1001):
        divis,remain,remain1,remain2=0,0,0,0
        if i in y.keys():
            summation+=len((y[i]))
            print("%d is called %s"%(i,y[i]))
        elif len(str(i))==2:
            divis=i-i%10
            remain=i%10
            summation+=len(y[divis])+len(y[remain])
            print("%d is called %s %s" %(i,y[divis],y[remain]))
        elif len(str(i))==3:
            divis=i/100
            remain=i%100
            if remain==0:
                summation+=len(y[divis])+len("hundred")
                print("%d is called %s Hundred" %(i,y[divis]))
            else:
                 if remain in y.keys():
                    summation+=len(y[divis])+len("hundredand")+len(y[remain])
                    print("%d is called %s Hundred and %s" %(i,y[divis],y[remain]))
                 else:
                    remain1=remain-remain%10
                    remain2=remain%10
                    summation+=len(y[divis])+len("hundredand")+len(y[remain1])+len(y[remain2])
                    print("%d is called %s Hundred and %s %s" %(i,y[divis],y[remain1],y[remain2]))

    print(summation)
if __name__ == '__main__':
    main()

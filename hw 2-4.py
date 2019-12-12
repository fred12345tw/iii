bonus=int(input())
earn=int(input())
bonusearn=int(input())
First=int(input())
Second=int(input())
Third=int(input())
cost=int(input())
#將變數命名，first,second,third 分別是三個時段的單數
totalcost=int()
totalearn=int()
totalreturn=int()
bestreturn=-10000
besttime=int()
#把要用來計算的各個變數命名，其中bestreturn只會保留跑往所有迴圈後最好的數字

i=1
#因為只少要工作一個時段，最多工作十二個時段，因此從一開始跑到十二，看工作多少時間有最大收益
while i <=12:
#分成三種情況對應三個不同累積時段的單數  
  if i <=4:
#每種都可能可以達到獎勵時數也可能不行，所以每種再分兩種情況討論 
    if First*i-bonus>=0:
#分成兩個來算:總單數*基本報酬加上多的時段*比基本報酬多的部分
      totalearn=(First*i)*earn+(First*i-bonus)*(bonusearn-earn)
    else:
      totalearn=(First*i)*earn
  elif 4<i<=8:
    if First*4+Second*(i-4)-bonus >=0:
      totalearn=(First*4+Second*(i-4))*earn+(First*4+Second*(i-4)-bonus)*(bonusearn-earn)
    else:
      totalearn=(First*4+Second*(i-4))*earn
  else:
    if First*4+Second*4+Third*(i-8)-bonus >=0:
      totalearn=(First*4+Second*4+Third*(i-8))*earn+(First*4+Second*4+Third*(i-8)-bonus)*(bonusearn-earn)   
    else:
      totalearn=(First*4+Second*4+Third*(i-8))*earn    
#總花費為時段數*每時段成本  
  totalcost=i*cost
  totalreturn=totalearn-totalcost
#除非工作多一小時能有更多報酬，不然不會覆蓋最佳報酬原本的數字
  if totalreturn>bestreturn:
    bestreturn=totalreturn
#當能夠覆蓋時紀錄那時候工作的時段數
    besttime=i  
  i+=1
#為了能夠把空格去掉要先把數字變字串
besttime=str(besttime)
bestreturn=str(bestreturn)  
#利用+把空格去掉
print(besttime+","+bestreturn)
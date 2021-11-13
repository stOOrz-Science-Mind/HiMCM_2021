dat=xlsread('C:\Users\Allan\Desktop\stOOrz Mathematical Modeling Group\水的饱和蒸汽压与温度对应表-精简版.xls')

for i=5:53
    temperature(i-4)=dat(i,1)
    pressure(i-4)=dat(i,2)
end


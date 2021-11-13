dat=xlsread('data3.xlsx')
x=71:86;
    y=dat(x,1);
    plot(x,y);
    
    hold on
    
    y=dat(x,2);
    plot(x,y);
    
    hold on
    
    y=dat(x,3);
    plot(x,y);
    
    hold on
    
    y=dat(x,4);
    plot(x,y);
    
    hold on
    
    y=dat(x,5);
    plot(x,y);
    
    hold on
    
    y=dat(x,6);
    plot(x,y);
    
    hold on
    
    y=dat(x,7);
    plot(x,y);
    
    hold on
    
    y=dat(x,8);
    plot(x,y);
    
    hold on
    
    y=dat(x,9);
    plot(x,y,'r--');
    
    hold on
    
    y=dat(x,10);
    plot(x,y,'y--');
    
    hold on
    
    y=dat(x,11);
    plot(x,y,'g--');
    
    hold on
    
    y=dat(x,12);
    plot(x,y,'b--');
    legend('January','February','March','April','May','June','July','August','September','October','November','December')
    hold off
    %12条曲线分别是1~12月历年水量折线图。%
 
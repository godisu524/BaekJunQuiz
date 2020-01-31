f_cost,v_cost,price = map(int, input().split())

num_sales = 0

if v_cost < price:
    num_sales = f_cost // (price - v_cost)   
    print (num_sales+1)
    
else:
    print(-1)
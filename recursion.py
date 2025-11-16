def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)
 
# call stack:  [{'input': 5}]
# call stack:  [{'input': 4}]
# call stack:  [{'input': 3}]
# call stack:  [{'input': 2}]
# base case reached! Num is 1.
# 120
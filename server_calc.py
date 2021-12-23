import socket
import sys
import time
import errno
import math        #Math Module
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("##### Online  Calculator Using Python #####\nHow to use: log/sqrt/exp/factorial<space><number>\n-------------------------------------------\nExample:\n log 123\n factorial 12\n\t\tType 'q' to terminate\n"))
    while True:
        data = s_sock.recv(2048)                        #input received from client
        data = data.decode("utf-8")                     #decode the data
        
        try:
            operation,number1= data.split(" ")  #this will split the input into two 
            op = str(operation)                 #the operation got splitted from the data and cast to strong
            num1 = int(number1)                 #the number1 input got spillted from the data and cast to integer
            
            if op[0] == 'l':
                answer = math.log(num1)         #math calculation here
            elif op[0] == 's':
                answer = math.sqrt(num1)
            elif op[0] == 'e':               
                answer = math.exp(num1)
            elif op[0] == 'f':               
                answer = math.factorial(num1)
            else:
                answer = ('Wrong input')  

            sendAnswer = ('Answer = '+str(answer))
            print ('Calculation Completed')
        except:
            print ('Wrong input')
            sendAnswer = ('Wrong input')

        if not data:
            break
            
        s_sock.send(str.encode(sendAnswer))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))                                   
    print("Listening...")
    s.listen(28)                                        
    
    try:
        while True:
            try:
                s_sock, s_addr= s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

            except Exception as e:        
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
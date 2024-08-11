import streamlit as st

def addition(a,b):
    c = a + b 
    return c

def subtraction(a,b):
    c = a - b
    return c

def multiplication(a,b):
    c = a * b 
    return c

def division(a,b):
    try:
        if  b == 0:
            raise ValueError(f"sorry your input {b} was invalid please try again")
        c = a / b 
        return c
    except ValueError as ve: 
        print(ve)

def modulos(a,b):
    try:
        if  b == 0:
            raise ValueError(f"sorry your input {b} was invalid please try again")
        c = a % b 
        return c
    except ValueError as ve: 
        print(ve)

def power(a,b):
    c = a**b
    return c 

def all(a,b):
    try:
        if  b == 0:
            raise ValueError(f"sorry your input {b} was invalid please try again")
        c = (a + b) + (a-b) + (a*b) + (a**b) + (a % b) + (a/b)
        return c
    except ValueError as ve: 
        print(ve)

def main():
    st.title(" Osman & Cisse's sophisticated calculator")
    st.write("Select an operation")
    operation = st.selectbox("Operation",["Add","Subtract","Multiply","Divide","Remainder","Power","All"])
    num1 = st.number_input("Enter the first number",format ="%.3f")
    num2 = st.number_input("Enter your second number",format ="%.3f")
    if st.button("Calculate"):
        if operation == "Add":
            result = addition(num1,num2)
        elif operation == "Subtract":
            result = subtraction(num1,num2)
        elif operation == "Multiply":
            result =  multiplication(num1,num2) 
        elif operation == "Divide":
            result =  division(num1,num2)                   
        elif operation == "Remainder":
            result =  modulos(num1,num2)                 
        elif operation == "Power":
            result = power(num1,num2)
        elif operation == "All":
            result = all(num1,num2)
         
        st.write(f"The operation you chose was {operation} an your result is {result}")            
            
if __name__ == "__main__":
    main()
    









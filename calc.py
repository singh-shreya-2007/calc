
import streamlit as st

def calculator(num1,num2,opr):
    if opr=="+":
        return num1+num2
    if opr=="-":
        return num1-num2
    if opr=="*":
        return num1*num2
    if opr=="/":
        if num2!=0:
              return num1/num2
        else:
            return "zero division error not possible"
    
def main():
    st.title("Calc")
        
    number1=st.number_input("enter your number.....,",format="%2f")
    operator=st.selectbox("select operator",["+","-","*","/"])
    number2=st.number_input("enter your number1.....,",format="%2f")


    result=calculator(number1,number2,operator)
    if st.button("calculate"):
        st.success(result)

if __name__=="__main__":
    main()
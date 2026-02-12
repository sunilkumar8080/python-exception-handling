try:
    n=input("Enter number:")
    print(f"the power of number{n}")
    for i in range(1,11):
        print(f"{int(n)}^{i}={int(n)**i}")
except Exception as e:
    print("invalid input🚫 please enter number")        
    
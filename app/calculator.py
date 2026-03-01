def calculator ():
    print("welcome to my calculator")
    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            if command == 'exit':
                print ("bye")
                break
        except Exception as e:
            print(f"Error while reading comman from user : {e}")         




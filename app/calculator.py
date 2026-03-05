from app.operations.operation_factory import OperationFactory

def calculator ():
    print("welcome to my calculator")
    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            if command == 'exit':
                print ("bye")
                break
            else:
                thisOperation = OperationFactory.create_operation(command)
                print(thisOperation.execute())

        except Exception as e:
            print(f"Error - {e}")         




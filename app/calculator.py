from ast import List

from app.operations.operation import Operation
from app.operations.operation_factory import OperationFactory

class Calculator:
 def __init__(self):
    self.history: List[Operation] = []
 
 def start(self):
    print("welcome to my calculator")
    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            if command == 'exit':
                print ("bye")
                break
            if command == 'history':
               if not self.history:
                  print("No calculations in history")
               else:
                  print("\nCalculations History:")
                  for i, entry in enumerate(self.history, 1):
                            print(f"{i}. {entry}")
            else:
                thisOperation = OperationFactory.create_operation(command)
                print(thisOperation.execute())
                self.history.append(thisOperation)

        except Exception as e:
            print(f"Error - {e}")         




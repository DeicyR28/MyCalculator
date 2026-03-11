from ast import List
import os
import logging
from pathlib import Path
from app.operations.operation import Operation
from app.operations.operation_factory import OperationFactory
import pandas as pd

class Calculator:
 def __init__(self):
    self.history: List[Operation] = []
    if self.get_history_file_path.exists():
         try:
           self.load_history()
         except Exception as e:
            logging.warning(f"Could not load existing history: {e}")
    

 def save_history(self) -> None:
   df = pd.DataFrame([op.to_dict() for op in self.history])
   if not df.empty: df.to_csv(self.get_history_file_path, index=False)

 def load_history(self) -> None:
     df = pd.read_csv(self.get_history_file_path)
     self.history = [ OperationFactory.create_operation_from_dict(row) for _, row in df.iterrows()]

 def clear_history(self) -> None:
  if self.get_history_file_path.exists():
    os.remove(self.get_history_file_path)
  if self.history:
    self.history.clear()


 @property
 def get_history_file_path(self) -> Path:
   app_root = Path(__file__).parent 
   return app_root / os.getenv("HISTORY_FILE_NAME")

         
 def start(self):
    print("welcome to my calculator")
    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            is_valid, result = self.validate_command(command)
            if not is_valid:
              print(result)

            elif command == 'help':
                    # Display available commands
                    print("\nAvailable commands:")
                    print("  add, subtract, multiply, divide, power, root, percent, intdiv, absdiv,  - Perform calculations")
                    print("  history - Show calculation history")
                    print("  clear - Clear all calculation history")
                    print("  Calculation history is auto saved to file")
                    print("  Calculation history is auto loaded if it was previusly saved")
                    print("  exit - Exit the calculator")
                    print(" example, enter command: add 5 10   And your result will be 15")
                    continue

            elif command == 'exit':
                self.save_history()
                print ("bye")
                break
                
            elif command == 'clear':
              self.clear_history()

            elif command == 'history':
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
  

 def validate_command(self,command_str):
    if command_str in ['help', 'exit', 'history', 'clear']:
        return True, None

    # 1. Split the string by whitespace
    parts = command_str.split()

    # 2. Check if there are exactly 3 parts (Operation, Num1, Num2)
    if len(parts) != 3:
        return False, "Error: Command must follow format 'Operation Num1 Num2' type 'help' for more info."

    operation = parts[0]
    if operation.lower() not in ['add', 'subtract', 'multiply', 'divide', 'power', 'root', 'percent', 'intdiv', 'absdiff']:
        return False, f"Error: Unsupported operation '{operation}'. Supported operations are: add, subtract, multiply, divide, power, root, percent, intdiv, absdiff."
    
    # 3. Try to convert the last two parts to numbers (floats handle decimals too)
    try:
        num1 = float(parts[1])
        num2 = float(parts[2])
    except ValueError:
        return False, "Error: The second and third values must be numbers."

    # 4. If everything passes, return the cleaned data
    return True, (operation, num1, num2)
        
      




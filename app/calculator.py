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

 @property
 def get_history_file_path(self) -> Path:
   app_root = Path(__file__).parent 
   return app_root / os.getenv("HISTORY_FILE_NAME")
         
 def start(self):
    print("welcome to my calculator")
    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            if command == 'exit':
                self.save_history()
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
         
      




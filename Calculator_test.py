def Calc_window():
  TestedApps.WindowsCalculator.Run()
  
  

 
def nums(param):
  num = Sys.Process("Microsoft.WindowsCalculator", 2).UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad")
  num_clicked = num.FindAllChildren("Classname","button", 10)
  for btn in num_clicked:
      if btn.ObjectIdentifier == param:
        btn.Click()
        Log.Message(f"{btn.ObjectIdentifier} is clicked")
        break
  else:
    Log.Warning("Couldn't click the button")
    
  
        
        
def std_ops(ops):
  op_char = Sys.Process("Microsoft.WindowsCalculator", 2).UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Standard_operators")
  char_ = op_char.FindAllChildren("Classname","button",10)
  for ch in char_:
    if ch.AutomationId == ops:
      ch.click()
      Log.Message(f'{ch.AutomationId} is clicked')
      break  
    else:
      Log.Warning("Couldn't click the button")
      
      
def perform_calcuations():
  nums("Two")
  std_ops("plusButton")
  nums("Three")
  std_ops("equalButton")
Calc_window()

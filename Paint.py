def open_window():
  TestedApps.MSPaint.Run()
  Delay(5000)
  new_project()
  
def new_project():
  new_file = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("New")
  file_1 = new_file
  file_1.Click()
  select_brush()
  
def select_brush():
  new_brush = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("Brushes").UIAObject("PrimarySidebar").UIAObject("ScrollViewer").UIAObject("Brushes").UIAObject("Marker")
  new_brush.Click()
  draw()
  
def draw():
  drawing = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("InteractorFocusWrapper").UIAObject("ZoomInteractor")
  drawing.Click()
  drawing.Drag(762,414,200,0)
  drawing.Drag(962,414,0,200)
  drawing.Drag(962,614,-200,0)
  drawing.Drag(762,614,0,-200)
  
  draws()
  
def draws():
  
  circle = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("D_shapes").UIAObject("PrimarySidebar").UIAObject("ScrollViewer").UIAObject("StickerPicker_Stickers_2DShapes").UIAObject("Circle")
  circle.Drag(762,414,200,0);
  
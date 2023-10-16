import maya.cmds
from functools import partial

storedPosValues = []
filePath = ""

def enableCheckbox(value):
	cmds.checkBox("returnObjects", edit=True, enable=value)
	if not value:
		cmds.checkBox("returnObjects", edit=True, enable=value, value=value)

def enableTextField(value):
	cmds.textField("exportPath", edit=True, enable=value)
	cmds.iconTextButton("openFileDialog", edit=True, enable=value)

def openFileBrowser():
	global filePath
	filePath = cmds.fileDialog2(fileMode=0)[0]
	cmds.textField("exportPath", edit=True, text=filePath)

def executeScript(moveObjects, exportObjects, returnObjects, *args):
	selectedObjects = cmds.ls(selection=True)
	storedPosValues.clear()

	if cmds.checkBox(moveObjects, query=True, value=True):	
		for object in selectedObjects:
			storedPosValues.append(cmds.getAttr("%s.translate" % object))
			cmds.move(0,0,0, object)

	if cmds.checkBox(exportObjects, query=True, value=True):
		cmds.file(filePath, force = True, options = "v = 0", type = "FBX export", exportSelected = True)

	if cmds.checkBox(returnObjects, query=True, value=True):
		for objectIndex, object in enumerate(selectedObjects):
			cmds.move(storedPosValues[objectIndex][0][0], storedPosValues[objectIndex][0][1], storedPosValues[objectIndex][0][2], object)

def createWin():
	widthWin=400
	columnWidthFirst=150
	window = cmds.window(title="Quick Transform and Export", width=widthWin)
	cmds.columnLayout(adjustableColumn=True)
	cmds.text(label="")

	cmds.rowColumnLayout(numberOfColumns=2, height=250, adjustableColumn=2, columnAlign=(1, "right"), columnWidth=((1, columnWidthFirst), (2, widthWin - columnWidthFirst)))

	cmds.text(label="Settings: ")
	moveObjects = cmds.checkBox(label="Move selected objects to origin", changeCommand=enableCheckbox)

	cmds.text(label="")
	returnObjects = cmds.checkBox("returnObjects", label="Return selected objects to original position", enable=False)
	
	cmds.text(label="")
	exportObjects = cmds.checkBox(label="Export selected objects", changeCommand=enableTextField)
	
	cmds.text("Export path: ")
	cmds.rowLayout(numberOfColumns=2, adjustableColumn=True)
	exportPath = cmds.textField("exportPath", enable=False)
	openFileDialog = cmds.iconTextButton("openFileDialog", label="...", image="browseFolder.png", command=openFileBrowser,  enable=False)
	cmds.setParent("..")

	cmds.setParent("..")

	cmds.button(label="Execute", command=partial(executeScript, moveObjects, exportObjects, returnObjects))

	cmds.showWindow(window)
createWin()
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = '10.26 Partial Reinforcement Effect'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1500, 1000), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
TIME = 30.000000 

trialClock = core.Clock()
Cue1 = visual.Rect(
    win=win, name='Cue1',
    width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=u'red', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

TargetStimulus = visual.Polygon(
    win=win, name='TargetStimulus',
    edges=99897, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=u'white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
FoodResponse = visual.TextStim(win=win, name='FoodResponse',
    text='FOOD :)',
    font='Arial',
    pos=(0,.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
Cue1_2 = visual.Rect(
    win=win, name='Cue1_2',
    width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=u'Blue', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

TargetStimulus_2 = visual.Polygon(
    win=win, name='TargetStimulus_2',
    edges=99897, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=u'white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
FoodResponse_2 = visual.TextStim(win=win, name='FoodResponse_2',
    text='FOOD :)',
    font='Arial',
    pos=(0,.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(TIME)
# update component parameters for each repeat

# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
# keep track of which components have finished
trialComponents = [Cue1, TargetStimulus, mouse, FoodResponse]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------

while continueRoutine and routineTimer.getTime() > 0:
   
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue1* updates
    if t >= 0.0 and Cue1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue1.tStart = t
        Cue1.frameNStart = frameN  # exact frame index
        Cue1.setAutoDraw(True)
    frameRemains = 0.0 + TIME- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Cue1.status == STARTED and t >= frameRemains:
        Cue1.setAutoDraw(False)
        
    if mouse.isPressedIn(TargetStimulus):
            FoodResponse.tStart = t
            FoodResponse.frameNStart = frameN 
            FoodResponse.setAutoDraw(True)
    
    if FoodResponse.status == STARTED and t >= (FoodResponse.tStart + 2):
            FoodResponse.setAutoDraw(False)
    
    # *TargetStimulus* updates
    if t >= 0.0 and TargetStimulus.status == NOT_STARTED:
        # keep track of start time/frame for later
        TargetStimulus.tStart = t
        TargetStimulus.frameNStart = frameN  # exact frame index
        TargetStimulus.setAutoDraw(True)
    frameRemains = 0.0 + TIME- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TargetStimulus.status == STARTED and t >= frameRemains:
        TargetStimulus.setAutoDraw(False)
    # *mouse* updates
    if t >= 0.0 and mouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse.tStart = t
        mouse.frameNStart = frameN  # exact frame index
        mouse.status = STARTED
        event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
    frameRemains = 0.0 + TIME- win.monitorFramePeriod * 0.75  # most of one frame period left
    if mouse.status == STARTED and t >= frameRemains:
        mouse.status = STOPPED
    if mouse.status == STARTED:  # only update if started and not stopped!
        buttons = mouse.getPressed()
        if sum(buttons) > 0:  # ie if any button is pressed
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(trialClock.getTime())
                   
    #RECORD Data 
    
    if mouse.isPressedIn(Cue1) and not (mouse.isPressedIn(TargetStimulus)):
        thisExp.addData('mouse1Time', t)
        thisExp.addData('mouse1position', mouse.getPos())
        thisExp.addData('ClicksTrial1', 0)
        thisExp.nextEntry()
        while mouse.isPressedIn(Cue1) and not (mouse.isPressedIn(TargetStimulus)):
            continue
        
    elif (mouse.isPressedIn(TargetStimulus)):
        thisExp.addData('mouse1Time', t)
        thisExp.addData('mouse1position', mouse.getPos())
        thisExp.addData('ClicksTrial1', 1)
        thisExp.nextEntry()
        while (mouse.isPressedIn(TargetStimulus)):
            continue
     
    
    # *FoodResponse* updates
    if (mouse.isPressedIn(TargetStimulus)) and FoodResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        FoodResponse.tStart = t
        FoodResponse.frameNStart = frameN  # exact frame index
        FoodResponse.setAutoDraw(True)

    if FoodResponse.status == STARTED and t >= (FoodResponse.tStart + 2):
        FoodResponse.setAutoDraw(False)
        

    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        

# ------Prepare to start Routine "trial2"-------
t = 0
trial2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat

# setup some python lists for storing info about the mouse_2
# keep track of which components have finished
trial2Components = [Cue1_2, TargetStimulus_2, mouse_2, FoodResponse_2]
for thisComponent in trial2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue1_2* updates
    if t >= 0.0 and Cue1_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue1_2.tStart = t
        Cue1_2.frameNStart = frameN  # exact frame index
        Cue1_2.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Cue1_2.status == STARTED and t >= frameRemains:
        Cue1_2.setAutoDraw(False)
    if mouse.isPressedIn(TargetStimulus):
            FoodResponse.tStart = t
            FoodResponse.frameNStart = frameN 
            FoodResponse.setAutoDraw(True)
    
    if FoodResponse.status == STARTED and t >= (FoodResponse.tStart + 2):
            FoodResponse.setAutoDraw(False)
    
    # *TargetStimulus_2* updates
    if t >= 0.0 and TargetStimulus_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        TargetStimulus_2.tStart = t
        TargetStimulus_2.frameNStart = frameN  # exact frame index
        TargetStimulus_2.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TargetStimulus_2.status == STARTED and t >= frameRemains:
        TargetStimulus_2.setAutoDraw(False)
        
    #RECORD Data 
    if mouse.isPressedIn(Cue1) and not (mouse.isPressedIn(TargetStimulus)):
        thisExp.addData('mouse2Time', t)
        thisExp.addData('mouse2position', mouse.getPos())
        thisExp.addData('ClicksTrial2', 0)
        thisExp.nextEntry()
        while mouse.isPressedIn(Cue1) and not (mouse.isPressedIn(TargetStimulus)):
            continue
    elif (mouse.isPressedIn(TargetStimulus)):
        thisExp.addData('mouse2Time', t)
        thisExp.addData('mouse2position', mouse.getPos())
        thisExp.addData('ClicksTrial2', 1)
        thisExp.nextEntry()
        while (mouse.isPressedIn(TargetStimulus)):
            continue
    
    # *FoodResponse_2* updates
    if (mouse.isPressedIn(TargetStimulus)) and FoodResponse_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        FoodResponse_2.tStart = t
        FoodResponse_2.frameNStart = frameN  # exact frame index
        FoodResponse_2.setAutoDraw(True)
    if FoodResponse_2.status == STARTED and t >= (FoodResponse_2.tStart + 2):
        FoodResponse_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial2"-------
for thisComponent in trial2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort() # make sure everything is closed down
win.close()
core.quit()

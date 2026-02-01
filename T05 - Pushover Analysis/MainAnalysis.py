

import openseespy.opensees as op
import matplotlib.pyplot as plt
import numpy as np


import ModelFunctions as mf
import AnalysisFunctions as af
import RecorderFunctions as rf
import PlotFunctions as pf


# ============================================================================
# Define Variables
# ============================================================================


pushoverLcForceName = 'Pushover_Lc_Force'
pushoverLcDispName = 'Pushover_Lc_Disp'
pushoverDcForceName = 'Pushover_Dc_Force'


runAnalysisLcf = True
runAnalysisLcD = True
runAnalysisDcf = True

NAnalysisSteps = np.array([209, 5000, 5000])

# ============================================================================
# Preprocessing
# ============================================================================





# ============================================================================
# Load control with force
# ============================================================================

op.wipe()

if runAnalysisLcf == True:
    
    
    # Build Model

    mf.getSections()
    mf.buildModel()
    # mf.plot_nodes()
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverLcForceName, pushoverLcForceName)
    af.PushoverLcf(int(NAnalysisSteps[0]))
    op.wipe()    
    
    # Plot Analysis
    pf.plotPushover(pushoverLcForceName, pushoverLcForceName)

# ============================================================================
# Load control with Disp
# ============================================================================


op.wipe()

if runAnalysisLcD == True:
    
    
    # Build Model

    mf.getSections()
    mf.buildModel()
    # mf.plot_nodes()
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverLcDispName, pushoverLcDispName)
    af.PushoverLcD(int(NAnalysisSteps[1]))
    op.wipe()    

    
    # Plot Analysis
    pf.plotPushover(pushoverLcDispName, pushoverLcDispName)



# ============================================================================
# Disp control with force
# ============================================================================


op.wipe()

if runAnalysisDcf == True:
    
    
    # Build Model

    mf.getSections()
    mf.buildModel()
    # mf.plot_nodes()
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverDcForceName, pushoverDcForceName)
    af.PushoverDcf(int(NAnalysisSteps[2]))
    op.wipe()    
        
    
    # Plot Analysis
    pf.plotPushover(pushoverDcForceName, pushoverDcForceName)






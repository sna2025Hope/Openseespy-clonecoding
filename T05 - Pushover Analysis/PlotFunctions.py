

import matplotlib.pyplot as plt
import numpy as np



def plotPushover(OutputDirName, AnalysisName):
    
    baseName = OutputDirName + '//' + AnalysisName
    dispFileName = baseName + '_Top_Dsp.out'
    reactionFileName = baseName + '_Reactions.out'

    Disp = np.loadtxt(dispFileName, delimiter= ' ')
    Reactions = np.loadtxt(reactionFileName, delimiter= ' ')
    
    x = Disp[:, 1]
    Shear = -Reactions[:, 1]

    
    fig, ax = plt.subplots()
    plt.plot(x, Shear)

    return Disp, Reactions



# OutputDirName = 'Pushover_Lc_Force'
# plotPushover(OutputDirName,OutputDirName)

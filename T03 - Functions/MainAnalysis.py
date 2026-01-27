# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 21:45:27 2026

@author: user
"""

import openseespy.opensees as op
from ModelFunctions import (GetSections, GetModel, GetRecordersPushover, 
                            RunAnalysisPushover, RunGravityAnalysis)

import numpy as np

# =============================================================================
# Units
# =============================================================================

m = 1
N = 1
Pa = 1

inches = 0.0254*m
ft = 12*inches
Kip = 4.45*10**3*N
Ksi = 6.89*10**6*Pa



# =============================================================================
# Input Variables
# =============================================================================


A1 = 10.*inches**2
A2 = 5.*inches**2

E = 3000*Ksi

Px = 100*Kip
Py = -50*Kip

# =============================================================================
# Run Analysis
# =============================================================================

analysisName = 'pushover'

GetSections(E)
GetModel(A1, A2)
GetRecordersPushover(analysisName)
RunAnalysisPushover(Px, Py)


analysisName = 'Gravity'

GetSections(E)
GetModel(A1, A2)
GetRecordersPushover(analysisName)
RunGravityAnalysis(Py)


# =============================================================================
# Area Optimization Analysis
# =============================================================================

targetDisp = -0.01*m

lowerBound = 1*inches**2
upperBound = 20*inches**2

Narea = 20
trialAreas = np.linspace(lowerBound,upperBound,Narea)
outputDisp = np.zeros([Narea,Narea])


for ii, A1 in enumerate(trialAreas):
    for jj, A2 in enumerate(trialAreas):
       GetSections(E)
       GetModel(A1, A2)
       RunGravityAnalysis(Py)
 
       outputDisp[ii,jj] = op.nodeDisp(4,2)
 
       op.wipe()




shiftOutput = np.abs(outputDisp - targetDisp)
[[MinIndexA1] ,[MinIndexA2] ] = np.where(shiftOutput == np.min(shiftOutput))


A1Optimal = trialAreas[MinIndexA1]
A2Optimal = trialAreas[MinIndexA2]


analysisName = 'Optimal_Area_Analysis_'
GetSections(E)
GetModel(A1Optimal, A2Optimal)
GetRecordersPushover(analysisName)
RunAnalysisPushover(Px, Py)

op.wipe()



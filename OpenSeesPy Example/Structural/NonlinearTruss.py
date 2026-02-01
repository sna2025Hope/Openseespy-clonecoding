from openseespy.opensees import *

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Start of model generation
# -----------------------------

# set modelbuilder
wipe()
model('basic', '-ndm', 2, '-ndf', 2)

# variables
A = 4.0
E = 29000.0
alpha = 0.05
sY = 36.0
udisp = 2.5
Nsteps = 1000
Px = 160.0
Py = 0.0

# create nodes
node(1, 0.0, 0.0)
node(2, 72.0, 0.0)
node(3, 168.0, 0.0)
node(4, 48.0, 144.0)

# set boundary condition
fix(1, 1, 1)
fix(2, 1, 1)
fix(3, 1, 1)

# define materials
# Hiso > 0 등방경화, Hkin < 0 이동경화, Both > 0 혼합경화
# Hiso = isotropic hardening Modulus
# Hkin = kinematic hardening Modulus
# sY = yield stress

uniaxialMaterial("Hardening", 1, E, sY, 0.0, alpha/(1-alpha)*E)

# define elements
element("Truss",1,1,4,A,1)
element("Truss",2,2,4,A,1)
element("Truss",3,3,4,A,1)

# create TimeSeries
timeSeries("Linear", 1)

# create a plain load pattern
# timeseries tag = 1, load scale factor = 1
pattern("Plain", 1, 1)

# Create the nodal load
load(4, Px, Py)

# ------------------------------
# Start of analysis generation
# ------------------------------

# create SOE
# SPD = Symmetric positive Definite
system("ProfileSPD")

# create DOF number
numberer("Plain")

# create constraint handler
constraints("Plain")

# create integrator
integrator("LoadControl", 1.0/Nsteps)

# create algorithm
algorithm("Newton")

# create test
# 잔차력(외력-내력) => tolerance(1e-8) 수렴여부 판단
# 10 = maxiteration (한 하중 스텝의 최대 반복수)
test('NormUnbalance',1e-8, 10)

# create analysis object
analysis("Static")

# ------------------------------
# Finally perform the analysis
# ------------------------------

# perform the analysis
# 결과 저장용 배열 생성
# 행: 해석스텝(0 ~ Nsteps)
# 열: 2개 (0: 수평변위, 1: 수평하중)

data = np.zeros((Nsteps+1,2))

for j in range(Nsteps):
    analyze(1)
    data[j+1,0] = nodeDisp(4,1)
    data[j+1,1] = getLoadFactor(1)*Px

plt.plot(data[:,0], data[:,1])
plt.xlabel('Horizontal Displacement')
plt.ylabel('Horizontal Load')
plt.show()
plt.plot(data[:,0], data[:,1], '-o', markersize=3)
plt.grid(True)
plt.title('Load–Displacement Curve at Node 4')
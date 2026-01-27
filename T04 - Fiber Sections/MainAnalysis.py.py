
import openseespy.opensees as op
import ModelFunctions as mf
import vfo.vfo as vfo

op.wipe()
mf.getSections()
mf.buildModel()
vfo.plot_model()

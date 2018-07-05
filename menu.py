import os
import nuke

m = nuke.menu("Nuke")
newmen = m.addMenu("Custom Tools")
p = newmen.addMenu("rush") 
p.addCommand("Open Rush Dashboard", "os.popen('/usr/local/rush/bin/irush')", "Alt+o")
p.addCommand("Submit Nuke File", "os.popen('/usr/local/rush/examples/python/submit_nuke.py')", "Alt+s")


# %%
# example code
# https://lounge.airnhschool.com/smd
from airnh.ctrl import PIDSimple, SimManager
import matplotlib.pyplot as plt
%matplotlib widget

custom_storage = {"ts":[], "pos":[], "vel":[], "ref_pos":[], "ref_vel":[], "ref_acc":[]}

class MyFirstController(PIDSimple):
    def __init__(self):
        super().__init__() # DO NOT Delete This Line

    def updateControlOutput(self, states_msg):
      
        ts = states_msg["time_stamp"]
        pos_curr = states_msg["position"]
        vel_curr = states_msg["velocity"]
        
        ctrl_out = 10

        custom_storage["ts"].append(ts) 
        custom_storage["pos"].append(pos_curr)
        custom_storage["vel"].append(vel_curr)

        return ctrl_out

sim_man = SimManager(timeout=5)
sim_man.register_controller(controller=MyFirstController())
sim_man.start()


#==============================================================================
# Plotting
ts = custom_storage["ts"]
pos = custom_storage["pos"]
vel = custom_storage["vel"]

plt.figure()
plt.plot(ts, pos, 'b')
plt.title('Position vs Time')

plt.figure()
plt.plot(ts, vel, 'b')
plt.title('Velocity vs Time')

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(ts, pos, vel, marker='o')
ax.set_xlabel("time, ts")
ax.set_ylabel("Position, m")
ax.set_zlabel("Velocity, m/s")

plt.show()

# %%

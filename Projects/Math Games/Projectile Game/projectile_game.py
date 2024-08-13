import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, FloatSlider, Button
import ipywidgets as widgets
import time
from IPython.display import display, clear_output

# Random wall parameters
wall_dist = np.random.uniform(5, 15)
wall_height = np.random.uniform(2, 10)

# Function to plot the path
def plot_parabola(angle, velocity):
    g = 9.8
    angle_rads = np.radians(angle)
    
    # Time array
    t_max = 2 * velocity * np.sin(angle_rads) / g
    t = np.linspace(0, t_max, num=100)
    
    x = velocity * np.cos(angle_rads) * t
    y = velocity * np.sin(angle_rads) * t - 0.5 * g * t**2
    
    # Initial plot with static trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Rocket's Path", color='b')
    plt.axvline(x=wall_dist, ymin=0, ymax=wall_height/max(y), color='r', linestyle='--', label='Wall')
    plt.scatter([wall_dist], [wall_height], color='red')  # Mark the top of the wall
    
    plt.xlim(0, max(x))
    plt.ylim(0, max(y) + 1)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Adjust the Path to Clear the Wall')
    plt.legend()
    plt.grid(True)
    plt.show()

# Sliders for angle and velocity
angle_slider = FloatSlider(min=0, max=90, step=1, value=45, description='Angle (degrees)')
velocity_slider = FloatSlider(min=5, max=50, step=1, value=25, description='Velocity (m/s)')

def animate(vel, ang):
    g = 9.80
    angle_rads = np.radians(ang)

    # Time array
    t_max = 2 * vel * np.sin(angle_rads) / g
    t = np.linspace(0, t_max, num=100)
    x = vel * np.cos(angle_rads) * t
    y = vel * np.sin(angle_rads) * t - 0.5 * g * t**2

    for i in range(len(x)):
        plt.figure(figsize=(10, 6))
        plt.plot(x[:i+1], y[:i+1], label="Rocket's Path", color='b')
        plt.axvline(x=wall_dist, ymin=0, ymax=wall_height/max(y), color='r', linestyle='--', label='Wall')
        plt.scatter([wall_dist], [wall_height], color='red')  # Mark the top of the wall
        
        # Rocket position at the current frame
        plt.scatter([x[i]], [y[i]], color='blue')
        
        # Plot settings
        plt.xlim(0, max(x))
        plt.ylim(0, max(y) + 1)
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.title('Projectile Motion of the Toy Rocket')
        plt.legend()
        plt.grid(True)
        
        display(plt.gcf())
        clear_output(wait=True)
        time.sleep(0.02)
        plt.close()

    wall_index = np.where(x >= wall_dist)[0][0]  # Find the index where x is just over the wall's position
    if y[wall_index] > wall_height:
        print("Success! The rocket clears the wall.")
    else:
        print("Fail! The rocket hits the wall.")

# Create interactive plot
interact(plot_parabola, angle=angle_slider, velocity=velocity_slider)

def on_button_click(b): animate(angle_slider.value, velocity_slider.value)

button = widgets.Button(description="Show Path")
button.on_click(on_button_click)
display(button)

# a = widgets.FloatText(value=0.1, description='a:')
# b = widgets.FloatText(value=-1, description='b:')
# c = widgets.FloatText(value=5, description='c:')
# display(a, b, c)

# def on_button_click(b): plot_manual_parabola(a_input.value, b_input.value, c_input.value)

# button = widgets.Button(description="Plot Parabola")
# button.on_click(on_button_click)
# display(button)
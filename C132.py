import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_with_gravity.csv")


mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius,mass)


plt.title("Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(gravity,mass)
plt.title("gravity & Mass of the Star")
plt.xlabel("gravity")
plt.ylabel("Mass")
plt.show()


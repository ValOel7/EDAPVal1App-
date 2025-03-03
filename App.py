import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#https://docs.streamlit.io/develop/quick-reference/cheat-sheet
st.title("This is my EDAP App")
# Generate random time series data
if st.button("Test this"):
  time_series = np.random.randn(100)
  st.subheader("This is the time series graph")
  # Plot the time series
  plt.plot(time_series)
  plt.title("Random 100-Unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Value")
  st.pyplot(plt.gcf())
st.markdown(
    """
    **Scale-Free Network Disease Spread Simulation**

    This simulation models disease spread in a **scale-free network** using an agent-based approach. 
    Nodes represent individuals, where **red indicates infection, green represents recovery, and blue signifies death**. 
    The spread follows **proximity-based transmission**, with larger nodes taking longer to infect smaller ones. 
    After 3 time steps, an infected node **recovers (turns green) or dies (turns blue) with a 50% probability**. 
    Users can adjust the number of agents, infection probability, and experiment duration.

    **Visualizations:**
    - A **real-time network graph** showing nodes changing color as infection progresses.
    - **Three smoothed time series plots**:
      - Infection spread over time (**Red**).
      - Number of recoveries per step (**Green**).
      - Number of deaths per step (**Blue**).

    Adjust parameters and run the simulation to observe how disease spreads in a complex network.
    """
)

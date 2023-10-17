# Importing necessary libraries
import streamlit as st

# Function to calculate dosing
def calculate_dose(weight, anesthetic, epinephrine):
    # The following are example maximum doses in mg/kg. Actual values may vary.
    # Always consult a medical professional or relevant literature for accurate values.
    dosages = {
        "Lidocaine": 3,
        "Lidocaine with Epinephrine": 7,
        "Bupivacaine": 2,
        "Bupivacaine with Epinephrine": 3,
    }
    
    # Get the dose per kg for the chosen anesthetic
    dose_per_kg = dosages.get(anesthetic + (" with Epinephrine" if epinephrine else ""), 0)
    
    # Calculate total dose
    return weight * dose_per_kg

# Streamlit app
st.title("Local Anesthetic Dosing Calculator")

# User inputs
weight = st.number_input("Enter patient's weight (kg):", min_value=0.0, value=70.0, step=0.1)
anesthetic = st.selectbox("Choose the local anesthetic:", ["Lidocaine", "Bupivacaine"])
epinephrine = st.checkbox("Using Epinephrine?")

# Calculate and display the dose
dose = calculate_dose(weight, anesthetic, epinephrine)
st.write(f"Maximum recommended dose of {anesthetic}{' with Epinephrine' if epinephrine else ''} for a patient of {weight} kg is: {dose} mg")

import json
import os
from iqm.qiskit_iqm import IQMProvider
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

print("Quantum circuit:")
bell.draw(output='text')  

def get_access_token():
    if os.path.exists('tokens.json'):
        with open('tokens.json', 'r') as f:
            config = json.load(f)
            return config.get('access_token')
    else:
        raise FileNotFoundError("ERROR: Couldn't find the 'tokens.json'.")

try:
    token = get_access_token()
    
    provider = IQMProvider(url="https://spark.quantum.linksfoundation.com/station", token=token)
    lagrange_backend = provider.get_backend()

    t_bell = transpile(bell, backend=lagrange_backend)
    
    print("Job started, waiting in hardware queue...")
    job = lagrange_backend.run(t_bell, shots=1024)
    print(f"Job ID: {job.job_id()}")

    result = job.result()
    counts = result.get_counts()
    
    print("Result of the IQM Lagrange:")
    print(counts)
    plot_histogram(counts)
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")


print("Simulator")
simulator = AerSimulator()
t_qc_sim = transpile(bell, simulator)
resultSim = simulator.run(t_qc_sim, shots=1024).result()
countSim = resultSim.get_counts()

print("Simulation results:", countSim)

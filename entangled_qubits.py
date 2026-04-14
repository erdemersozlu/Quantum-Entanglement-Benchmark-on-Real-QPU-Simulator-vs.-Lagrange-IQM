import json
import os
from iqm.qiskit_iqm import IQMProvider
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

print("quantum circuit:") #just for checking
print(bell.draw())

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
    
    print("İşlem başlatıldı, donanım sırası bekleniyor...")
    job = lagrange_backend.run(t_bell, shots=1024)
    print(f"İşlem ID (Job ID): {job.job_id()}")

    result = job.result()
    counts = result.get_counts()
    
    print("Result of the iqm lagrange")
    plot_histogram(counts)

except Exception as e:
    print(f"Bir hata oluştu: {e}")


print("simulator")
simulator = AerSimulator()
t_qc_sim = transpile(qc, simulator)
resultSim = simulator.run(t_qc_sim, shots=1024).result()
countSim = resultSim.get_counts()

print("simulation results:", countSim)


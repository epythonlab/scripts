#  Develop Your First Quantum Application with Python

# first, install qiskit-aer 
import qiskit

# Create a quantum circuit with two qubits
circuit = qiskit.QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit
circuit.h(0)

# Create classical registers and allocate classical bits
creg = qiskit.ClassicalRegister(2, name='c')
circuit.add_register(creg)

# Measure the qubits and store the measurement results in the classical bits
circuit.measure([0, 1], [creg[0], creg[1]])

# Simulate the circuit
simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit, simulator).result()

# Get the measurement results
counts = result.get_counts()
print(counts)




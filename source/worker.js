// Listen for messages from the main thread
self.onmessage = async function(event) {
    // Initialise Pyodide
    const pyodide = await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.18.1/full/' });

    // Run the Python code
    pyodide.runPythonAsync('print("Hello from Python!")').then(() => {
        console.log('Python script completed');
        self.postMessage({ result: 'Script completed' });
    }).catch((err) => {
        console.error('Error:', err);
        self.postMessage({ error: err.message });
    });
};
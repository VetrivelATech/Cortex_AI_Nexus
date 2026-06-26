import { useState } from "react";

function App() {
  const [result, setResult] = useState(null);

  const predictPlacement = async () => {
    const response = await fetch("http://127.0.0.1:8000/predict-placement", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        resume_score: 85,
        dsa_score: 70,
        project_score: 90,
        communication_score: 80,
        consistency_score: 75,
      }),
    });

    const data = await response.json();
    console.log("DATA =", data);
    setResult(data);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>CORTEX AI NEXUS TEST</h1>

      <button onClick={predictPlacement}>
        Predict
      </button>

      <br /><br />

      {result ? (
        <div>
          <h2>Probability: {result.placement_probability}%</h2>
          <h3>Status: {result.status}</h3>
        </div>
      ) : (
        <p>No result yet</p>
      )}
    </div>
  );
}

export default App;
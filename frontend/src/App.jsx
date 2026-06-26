import { useState } from "react";
import "./App.css";
import UploadResume from "./components/UploadResume";

function App() {
  const [form, setForm] = useState({
    resume_score: "",
    dsa_score: "",
    project_score: "",
    communication_score: "",
    consistency_score: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: Number(e.target.value),
    });
  };

  const predictPlacement = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/predict-placement", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="container">
      <div className="card">

        <h1>CORTEX AI NEXUS</h1>

        <input
          name="resume_score"
          placeholder="Resume Score"
          onChange={handleChange}
        />

        <input
          name="dsa_score"
          placeholder="DSA Score"
          onChange={handleChange}
        />

        <input
          name="project_score"
          placeholder="Project Score"
          onChange={handleChange}
        />

        <input
          name="communication_score"
          placeholder="Communication Score"
          onChange={handleChange}
        />

        <input
          name="consistency_score"
          placeholder="Consistency Score"
          onChange={handleChange}
        />

        <button onClick={predictPlacement}>Predict Now</button>

        {result && (
          <div className="result-box">

            <h2 className="score">
              {result.placement_probability}%
            </h2>

            <p className="status">{result.status}</p>

            <div className="section">
              <h3>Weak Areas</h3>
              {result.weak_areas.map((item, index) => (
                <p className="tag" key={index}>{item}</p>
              ))}
            </div>

            <div className="section">
              <h3>Recommendations</h3>
              {result.recommendations.map((item, index) => (
                <p className="tag" key={index}>{item}</p>
              ))}
            </div>

          </div>
        )}

        <UploadResume />

      </div>
    </div>
  );
}

export default App;
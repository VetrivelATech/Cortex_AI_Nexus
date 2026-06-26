import { useState } from "react";

function UploadResume() {
  const [result, setResult] = useState(null);

  const uploadResume = async (e) => {
    const file = e.target.files[0];

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze-resume",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setResult(data);

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="resume-box">

      <input type="file" onChange={uploadResume} />

      {result && (
        <div>

          <h2>ATS Score: {result.ats_score}%</h2>

          <h3>Detected Skills</h3>
          {result.detected_skills.map((skill, index) => (
            <p className="tag" key={index}>{skill}</p>
          ))}

          <h3>Missing Skills</h3>
          {result.missing_skills.map((skill, index) => (
            <p className="tag" key={index}>{skill}</p>
          ))}

        </div>
      )}

    </div>
  );
}

export default UploadResume;
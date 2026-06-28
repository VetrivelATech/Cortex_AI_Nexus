import { useState } from "react";

function GithubAnalyzer() {
  const [username, setUsername] = useState("");
  const [githubData, setGithubData] = useState(null);

  const analyzeGithub = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/analyze-github/${username}`
      );

      const data = await response.json();
      console.log(data);
      setGithubData(data);

    } catch (error) {
      console.error("GitHub error:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter GitHub Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button onClick={analyzeGithub}>
        Analyze GitHub
      </button>

      {githubData && (
        <div>
          <h3>GitHub Analysis</h3>
          <p>Repos: {githubData.repos}</p>
          <p>Followers: {githubData.followers}</p>
        </div>
      )}
    </div>
  );
}

export default GithubAnalyzer;
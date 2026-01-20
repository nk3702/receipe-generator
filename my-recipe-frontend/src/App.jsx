import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [ingredients, setIngredients] = useState("");
  const [recipe, setRecipe] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post("/generate_recipe", { ingredients });
      setRecipe(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Error generating recipe");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Recipe Generator</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          placeholder="Enter ingredients (e.g., tomato, cheese)"
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate"}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {recipe && (
        <div className="recipe">
          <h2>{recipe.recipe_title}</h2>
          <ol>
            {recipe.steps.map((step, idx) => (
              <li key={idx}>{step}</li>
            ))}
          </ol>
          <p>{recipe.additional_tips}</p>
        </div>
      )}
    </div>
  );
}

export default App;

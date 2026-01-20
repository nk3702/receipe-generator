import React, { useState } from "react";
import axios from "axios";

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
      setError(
        err.response?.data?.detail ||
          "Failed to generate recipe. Check if backend is running.",
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-xl p-8 w-full max-w-lg">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">
          Recipe Generator
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            value={ingredients}
            onChange={(e) => setIngredients(e.target.value)}
            placeholder="e.g., tomato, cheese, bread"
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <button
            type="submit"
            disabled={loading}
            className={`w-full py-3 px-4 rounded-lg text-white font-medium transition-colors ${
              loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loading ? "Generating..." : "Generate Recipe"}
          </button>
        </form>

        {error && (
          <div className="mt-6 p-4 bg-red-50 border border-red-200 text-red-700 rounded-lg">
            {error}
          </div>
        )}

        {recipe && (
          <div className="mt-8">
            <h2 className="text-2xl font-semibold text-green-700 mb-4">
              {recipe.recipe_title}
            </h2>
            <ol className="list-decimal pl-6 space-y-2 text-gray-700">
              {recipe.steps.map((step, idx) => (
                <li key={idx}>{step}</li>
              ))}
            </ol>
            {recipe.additional_tips && (
              <p className="mt-6 text-gray-600 italic">
                <strong>Tips:</strong> {recipe.additional_tips}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

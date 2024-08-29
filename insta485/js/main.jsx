import React from "react";
import { createRoot } from "react-dom/client";
import MainPage from "./mainPage";

// Create a root
const root = createRoot(document.getElementById("reactEntry"));

// This method is only called once
// Insert the post component into the DOM
root.render(<MainPage />);

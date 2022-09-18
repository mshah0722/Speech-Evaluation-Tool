import React from "react";
import VideoAnalysis from "./components/VideoAnalysis/VideoAnalysis";
import Header from "./components/Header/header.component";
import NavBar from "./components/Navbar/Navbar.component";

const App = () => (
  <div>
    <NavBar></NavBar>
    <Header></Header>
    <VideoAnalysis />
  </div>
);

export default App;

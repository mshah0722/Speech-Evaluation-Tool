import React from "react";
import FileUploadForm from "./components/FileUploadForm/FileUploadForm";
import Header from "./components/Header/header.component";
import NavBar from "./components/Navbar/Navbar.component";

const App = () => (
  <div>
    <NavBar></NavBar>
    <Header></Header>
    <FileUploadForm />
  </div>
);

export default App;

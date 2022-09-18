import React, { useState } from "react";
import { HeaderDiv } from "./header.styles";
import logo from "../../assets/Orator ME.png";

const Header = () => {
  return (
    <HeaderDiv>
      <div style={{ width: "50%", fontSize: "2.5em", textAlign: "center" }}>
        Want to improve your speaking skills and give the best pitch ever?
      </div>
      <div
        style={{
          width: "50%",
          fontSize: "1.5em",
          textAlign: "center",
          margin: "1em 0em 0em 0em",
        }}
      >
        Use our AI analysis to get instant feedback for your pitch!
      </div>
    </HeaderDiv>
  );
};

export default Header;

import React, { useState } from "react";
import { ContainerDiv, Box, RedLine, Line } from "./SimilarSentences.styles";

const SimilarSentences = () => {
  const data = [
    {
      first:
        "A strong self-introduction will help new acquaintances learn the most essential details about who you are in a way that’s engaging and memorable. ",
      mid: "In this article we define a self-introduction and offer you tips and examples so you can write your own effective self-introduction. ",
      last: "When you deliver a powerful self-introduction, you can make a lasting positive impression on people.",
    },
  ];
  return (
    <ContainerDiv>
      {data.map((elem, index) => (
        <Box key={index}>
          <Line>
            <span style={{ fontWeight: "600", color: "#ff595e" }}>
              {elem.first}
            </span>
            {elem.mid}
            <span style={{ fontWeight: "600", color: "#ff595e" }}>
              {elem.last}
            </span>
          </Line>
        </Box>
      ))}
    </ContainerDiv>
  );
};

export default SimilarSentences;

import React, { useState } from "react";
import { ContainerDiv, Box, RedLine, Line } from "./SimilarSentences.styles";

const SimilarSentences = () => {
  const data = [
    {
      first: "Hello my name is jpanintj. ",
      mid: "Hello my name is jpanintj. ",
      last: "Hello my name is jpanintj.",
    },
    { first: "Hello", mid: "10", last: "#fcf6bd" },
    { first: "Hello", mid: "10", last: "#d0f4de" },
    { first: "Hello", mid: "10", last: "#e4c1f9" },
  ];
  return (
    <ContainerDiv>
      {data.map((elem) => (
        <Box>
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

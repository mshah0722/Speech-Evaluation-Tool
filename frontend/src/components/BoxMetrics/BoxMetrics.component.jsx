import React, { useState } from "react";
import { ContainerDiv, Box, Number, Text } from "./BoxMetrics.styles";

const BoxMetrics = ({ metrics, labels }) => {
  console.log(metrics);
  console.log(labels);
  const data = [
    { number: metrics[0] + "%", text: labels[0], color: "pink" },
    { number: metrics[1], text: labels[1], color: "#fcf6bd" },
    { number: metrics[2], text: labels[2], color: "#d0f4de" },
    { number: metrics[3], text: labels[3], color: "#e4c1f9" },
  ];
  return (
    <ContainerDiv>
      {data.map((elem, index) => (
        <Box key={index} color={elem.color}>
          <Number>{elem.number}</Number>
          <Text>{elem.text}</Text>
        </Box>
      ))}
    </ContainerDiv>
  );
};

export default BoxMetrics;

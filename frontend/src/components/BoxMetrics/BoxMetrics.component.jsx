import React, { useState } from "react";
import { ContainerDiv, Box, Number, Text } from "./BoxMetrics.styles";

const BoxMetrics = () => {
  const data = [
    { text: "Hello", number: "10", color: "pink" },
    { text: "Hello", number: "10", color: "#fcf6bd" },
    { text: "Hello", number: "10", color: "#d0f4de" },
    { text: "Hello", number: "10", color: "#e4c1f9" },
  ];
  return (
    <ContainerDiv>
      {data.map((elem) => (
        <Box color={elem.color}>
          <Number>{elem.number}</Number>
          <Text>{elem.text}</Text>
        </Box>
      ))}
    </ContainerDiv>
  );
};

export default BoxMetrics;

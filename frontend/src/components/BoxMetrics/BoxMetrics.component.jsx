import React, { useState } from "react";
import { ContainerDiv, Box, Number, Text } from "./BoxMetrics.styles";

const BoxMetrics = () => {
  const data = [
    { text: "Hello", number: "10" },
    { text: "Hello", number: "10" },
    { text: "Hello", number: "10" },
    { text: "Hello", number: "10" },
  ];
  return (
    <ContainerDiv>
      {data.map((elem) => (
        <Box>
          <Number>{elem.number}</Number>
          <Text>{elem.Text}</Text>
        </Box>
      ))}
    </ContainerDiv>
  );
};

export default BoxMetrics;

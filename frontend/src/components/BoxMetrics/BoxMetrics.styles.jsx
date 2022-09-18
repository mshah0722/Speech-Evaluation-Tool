import styled, { css, keyframes } from "styled-components";
import { Link } from "react-router-dom";

export const ContainerDiv = styled.div`
  width: 100%;
  padding: 1em 3em;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
`;

export const Box = styled.div`
  flex: 0.2;
  background-color: ${(props) => props.color};
  border-radius: 10px;
  padding: 1em;
  box-sizing: border-box;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const Number = styled.div`
  font-size: 3em;
  font-weight: 600;
  padding-bottom: 0.5em;
`;

export const Text = styled.div`
  font-size: 1em;
`;

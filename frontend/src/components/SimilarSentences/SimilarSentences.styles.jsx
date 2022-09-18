import styled, { css, keyframes } from "styled-components";
import { Link } from "react-router-dom";

export const ContainerDiv = styled.div`
  width: 100%;
  padding: 1em 3em;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
`;

export const Box = styled.div`
  flex: 0.5;
  background-color: ${(props) => props.color};
  border-radius: 10px;
  padding: 2em;
  box-sizing: border-box;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const RedLine = styled.div`
  font-size: 1.5em;
  font-weight: 600;
  color: #ff595e;
`;

export const Line = styled.div`
  font-size: 1.5em;
`;

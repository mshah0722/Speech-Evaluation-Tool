import styled from "styled-components";

export const FormDiv = styled.div`
  width: 100%;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`;

export const Button = styled.button`
  background: #48cae4;
  color: white;
  text-decoration: none;
  text-transform: uppercase;
  font-size: 0.85em;
  padding: 0.5em 2em;
  margin: 0em 0em 2em 0em;
  border-radius: 25px;
  font-weight: bold;
  display: flex;
  border: none;
  align-items: center;
  &:hover {
    opacity: 80%;
    cursor: pointer;
  }
  @media screen and (max-width: 1024px) {
    font-size: 0.75em;
    text-align: center;
  }
  @media screen and (max-width: 576px) {
    display: none;
  }
`;

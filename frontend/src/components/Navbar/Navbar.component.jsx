import React, { useState } from "react";
import {
  Hamburger,
  Navbar,
  NavContent,
  NavItem,
  NavItems,
  NavLink,
  NavLogo,
  NavLinkButton,
} from "./Navbar.styles";
import logo from "../../assets/Orator ME.png";

const NavBar = () => {
  return (
    <Navbar>
      <img src={logo} style={{ height: "4em" }} />
    </Navbar>
  );
};

export default NavBar;

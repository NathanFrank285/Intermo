import React from "react";
import './Footer.css'

function Footer() {
  return (
    <div
      className='footer-container'
    >
      {/* <img
        style={{ height: "10vh", width: "100px", borderRadius: "20px" }}
        // src={github}
        alt=""
      ></img> */}
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
        }}
      >
        <div style={{ marginTop: "10px" }}>Developed by Nathan Frank</div>
      </div>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
        }}
      >
        <a
          style={{ marginTop: "10px" }}
          href="https://github.com/NathanFrank285"
        >
          GitHub
        </a>
        <a
          style={{ marginTop: "10px", marginLeft: "10px" }}
          href="https://www.linkedin.com/in/nathan-frank-8a743568/"
        >
          LinkedIn
        </a>
      </div>
    </div>
  );
}

export default Footer;

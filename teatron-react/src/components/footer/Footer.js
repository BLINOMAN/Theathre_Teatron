import "./style.css"

import logo1 from "./../../img/icons/Vector-1.svg";
import logo2 from "./../../img/icons/Vector-2.svg";
import logo3 from "./../../img/icons/Vector.svg";

const Footer = () => {
  return ( 
    <footer className = "footer">
        <div className="container">
          <div className="footer-wrapper">
            <ul className="social">
              <li className="social-item">
                <a href="#!">
                  <img src={logo1} alt=""/>
                </a>
              </li>
              <li className="social-item">
                <a href="#!">
                  <img src={logo2} alt=""/>
                </a>
              </li>
              <li className="social-item">
                <a href="#!">
                  <img src={logo3} alt=""/>
                </a>
              </li>
            </ul>
            <div className="copiright">
              <p>© 2023 teatron.com</p>
            </div>
          </div>
        </div>
      </footer>
   
  );
}
 
export default Footer;

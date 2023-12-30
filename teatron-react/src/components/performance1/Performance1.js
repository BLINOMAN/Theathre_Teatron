import { NavLink } from "react-router-dom";
const Performance1 = ({index, img, title}) => {
  return ( 
  <NavLink to = {`/performance/${index}`}>
      <li className="project">
      <a className = "project__link" href="./project-page.html">
      <img src= {img} alt="Projects" className="project__img"/>
      <h3 className="project__title">{title}</h3>
    </a>
    </li> 
  </NavLink>

  );
}
 
export default Performance1;
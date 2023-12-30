import "./style.css"
import { NavLink } from "react-router-dom";
const Navbar = () => {
  const normalLink = "nav-list__link";
  const activeLink = "nav-list__link nav-list__link--active";
  return ( 
    <nav className="nav">
      <div className="container">
        <div className="nav-row">
          <NavLink to ="/" className = "logo"><strong>Театрон</strong></NavLink>
          <ul className="nav-list">
            <li className="nav-list__item"><NavLink to = "/" className={({isActive}) => isActive? activeLink : normalLink}>Спектакли</NavLink></li>
            <li className="nav-list__item"><NavLink to = "/history" className= {({isActive}) => isActive? activeLink : normalLink}>О театре</NavLink></li>
            <li className="nav-list__item"><NavLink to = "/staff" className= {({isActive}) => isActive? activeLink : normalLink}>Труппа</NavLink></li>
          </ul>
        </div>
      </div> 
    </nav>
   );
}
 
export default Navbar;
import "./style.css";
const Header = () => {
  function scrolldown(){
    const section = document.querySelector(".section");
    section.scrollIntoView({behavior: "smooth"});
  }

  return ( 
    <header className="header">
          <div className="header__wrapper">
            <h1 className="header__title">
              <strong>Афиши<em> Театрона</em></strong><br/>
            </h1>
            <div className="header__text">
              <p>Смотрите, бронируйте, наслаждайтесь...</p>
            </div>
            <a href="#!" className="btn" onClick={scrolldown}>По клику по кнопке</a>
          </div>
      </header>
   );
}
 
export default Header
;
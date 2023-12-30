import Header from "../components/header/Header";
import Performance1 from "../components/performance1/Performance1";
import { performanceList } from "../helpers/performanceList";
import NewsSection from "../components/NewsSection/NewsSection";




const Posters = () => {
  return ( 
    <>
      <Header/>
      <section className = "section">
        <div className="container">
          <h2 className="title-1">Ближайшие спектакли</h2>
          <ul className="projects">
            {performanceList.map((element, index) => { 
                return (
                <Performance1 key = {index} index = {index} img = {element.img} title = {element.title} />
                );
            })}
          </ul>
        </div>
      </section>
      <NewsSection/>
    </>
   );
}
 
export default Posters;
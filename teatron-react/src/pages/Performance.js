import { useParams } from "react-router-dom";
import { performanceList } from "../helpers/performanceList";
import logo from "./../img/icons/x3581862-1466412291.png";


const Performance = () => {
  const {id} = useParams();
  const performance = performanceList[id];
  return ( 
    <main className = "section">
      <div className="container">
        <div className="project-details">
          <h1 className="title-1">{performance.title}</h1>
          <img src= {performance.img} alt="" className="project-details__img"/>
          <div className="project-details__desc">
            <p className = "text">текст текст текст текст текст текст текст текст текст текст текст текстт екс т т е к сттексттекстт ексттексттекс ттекстт екст тексттек сттекс ттекстт екстте ксттек сттекстт екстте ксттекс ттекстте ксттекст тексттекстт ексттекстт екстте кст те к сттекст текс ттекс ттекс ттекс ттекст текстт екстте ксттек сттекстт екстте ксттек сттекст 
            </p>
          </div>
          <a href="https://afisha.yandex.ru/yekaterinburg/theatre/places/teatron-ekaterinburg?source=search-page" className="btn btn-outline">
            <img className = "btn__image" src= {logo} alt=""/>
            Купить билеты в афише
          </a>
        </div>
      </div>
  </main>
   );
}
 
export default Performance; 
import "./style.css";
import photo from "./../../img/project/03.jpg";

function NewsPoster(){
  return(
            <div class="staff-block">
              <img src={photo} alt="" class="project-details__img"/>
              <div class="project-details__desc">
                <h3>
                  Название новостного события
                </h3>
                <p class = "text-staff">
                  Описание описание описание описание Описание описание описание описание Описание описание описание описание Описание описание описание описание Описание описание описание описание
                </p>
              </div>
            </div>
    
  )
}


function NewsSection(){
  return(
    <main class = "section">
    <div class="container">
        <h1 class="title-1">Новости и события</h1>
        <div class = "staff-row">
          <NewsPoster/>
          <NewsPoster/>
          <NewsPoster/>
          <NewsPoster/>
        </div>
    </div>
  </main>
  )
}

export default NewsSection
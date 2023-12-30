import "./styles/main.css";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/navbar/Navbar";
import Footer from "./components/footer/Footer";
import Posters from "./pages/Posters";
import History from "./pages/History";
import Performance from "./pages/Performance";
import Staff from "./pages/Staff";
import ScrollToTop from "./utils/scrollToTop";




function App() {
  return (
    <div className="App">
      <Router>
        <ScrollToTop/>
        <Navbar/>
        <Routes>
          <Route path = "/" element = {<Posters/>}/>
          <Route path = "/performance/:id" element = {<Performance/>}/>
          <Route path = "/history" element = {<History/>}/>
          <Route path = "/staff" element = {<Staff/>}/>
        </Routes>
        <Footer/>
      </Router>

    </div>
  );
}

export default App;

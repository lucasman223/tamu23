import './App.scss';
import Layout from './components/Layout';
import About from "./components/About";
import { Routes, Route} from 'react-router-dom'

function App() {
  return (
    <>
    <Layout/>
    <Routes>
      
      <Route path="/about" element={<About/>} />
    </Routes>
    </>
  );
}

export default App;

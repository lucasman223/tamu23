import Layout from './components/Layout';
import About from "./components/About";
import { Routes, Route} from 'react-router-dom'
import Home from './components/Home'
import Result from './components/Result'

function App() {
  return (
    <>
    <Layout/>
    <Routes>
      
      <Route path="/about" element={<About/>} />
      <Route path="/" element={<Layout/>} />
      <Route path="/Result" element={<Result/>} />
      <Route index element={<Home/>} />
    </Routes>
    </>
  );
}

export default App;

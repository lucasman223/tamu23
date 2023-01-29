import React, { useEffect, useState } from 'react';
import axios from 'axios'

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



//import logo from './logo.svg';
//import './App.css';


// function App() {
//   const [getMessage, setGetMessage] = useState({})

//   useEffect(()=>{
//     // axios.post('http://localhost:5000', {
//     // fnum: '123',
//     // date: '13/22/22'
//     // }).then(response => {
//     //   console.log("SUCCESS", response)
//     //   setGetMessage(response)
//     // }).catch(error => {
//     //   console.log(error)
//     // })
//     axios.get('http://localhost:5000/flask/hello').then(response => {
//       console.log("SUCCESS", response)
//       setGetMessage(response)
//     }).catch(error => {
//       console.log(error)
//     })

//   }, [])
//   // return (
//   //   <div className="App">
//   //     <header className="App-header">
//   //       {/* <img src={logo} className="App-logo" alt="logo" /> */}
//   //       <p>React + Flask Tutorial</p>
//   //       <div>{getMessage.status === 200 ? 
//   //         <h3>{getMessage.data.message}</h3>
//   //         :
//   //         <h3>LOADING</h3>}</div>
//   //     </header>
//   //   </div>
//   // );
// }

// export default App;
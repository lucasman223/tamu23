import React, { useState } from 'react';
import './App.scss';
import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'

function App() {
  const [data,setData]=useState(null)
  const [print,setPrint]=useState(false)
  function getData(val)
  {
    setData(val.target.value)
    setPrint(false)
    console.warn(val.target.value)

  }
  return (
    <div className="App">
        {print ?
          <h1>{data}</h1>

          : null}
        <input type="text" onChange={getData} />
        <button onClick={() => setPrint(true)}>Check Flight</button>
      </div>
  );
}

export default App;

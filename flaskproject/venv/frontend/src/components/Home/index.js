import './index.scss';
import Sidebar from '../Sidebar';
import { Outlet } from 'react-router-dom'
import Layout from '../Layout';
import { useNavigate } from "react-router-dom";
import { useState } from 'react';
import axios from 'axios';

import { useSpring, animated } from '@react-spring/web'

// useEffect(()=>{
//       axios.post('http://localhost:5000', {
//       fnum: '123',
//       date: '13/22/22'
//       }).then(response => {
//         console.log("SUCCESS", response)
//         setGetMessage(response)
//       }).catch(error => {
//         console.log(error)
//       })

//     }, [])
const Home = () => {
  const [flightNum, setFlightNum] = useState("");
  const [date, setDate] = useState("");
  const [backendData, setBackendData] = useState({});


    const springs = useSpring({
        from: { x: -3000 },
        to: { x: 100 },
      })

let navigate = useNavigate();
const routeChange = () =>{ 
  let path = `/Result`; 
  navigate(path);
}

  function submit()
  {
    axios.post('http://localhost:5000', {
      flightNum: flightNum,
      date: date
    })
    .then(function (response) {
      let bd = response.data;
      console.log(bd)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

    return (
            

            <><Layout />
          <div className='container home-page'>
            <div className='text-zone'>
            <animated.div
            style={{
              width: 250,
              height: 500,
              borderRadius: 8,
              ...springs,
            }}>
              <h1>FlightForecast </h1> 
              <h2>Determining the Likelihood of Flight Delays Due to Weather Conditions 
                {/* FIND HOW TO INCREASE WIDTH SO ITS NOT AS VERTICAL */}
                </h2></animated.div>
                </div>
                <div className="form-group">
                <div>
                  <label>Enter Your Flight Number <br />
                    <input name="flightnum" placeholder='Ex. 748' value={flightNum} onChange={(event) => setFlightNum(event.target.value)}/>
                    <p>{flightNum}</p>
                  </label>
                  <label>Enter the Date of Flight <br />
                    <input name="date" placeholder='Ex. 1/29/2023' value={date} onChange={(event) => setDate(event.target.value)}/>
                    <p>{date}</p>
                  </label>
                  <button type='submit' onClick={submit}>Submit</button>
                </div>
          
            </div>
        </div>
        </>
    )
}

export default Home
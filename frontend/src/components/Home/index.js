import './index.scss';
import Sidebar from '../Sidebar';
import { Outlet } from 'react-router-dom'
import Layout from '../Layout';
import { useNavigate } from "react-router-dom";



import { useSpring, animated } from '@react-spring/web'

const Home = () => {
    const springs = useSpring({
        from: { x: -3000 },
        to: { x: 100 },
      })

let navigate = useNavigate();
const routeChange = () =>{ 
  let path = `/Result`; 
  navigate(path);
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
                <form>
                  <label>Enter Your Flight Number <br />
                    <input name="flightnum" placeholder='Ex. DAL748'/>
                  </label>
                  <button type='submit' onClick={routeChange}>Submit</button>
                </form>
              
            </div>
        </div>
        </>
    )
}

export default Home
import './index.scss';
import Sidebar from '../Sidebar';
import { Outlet } from 'react-router-dom'
import Layout from '../Layout';


import { useSpring, animated } from '@react-spring/web'

const PythonShell = require('python-shell');
const options = {
  scriptPath: 'path/to/python/script'
};
const Home = () => {
    const springs = useSpring({
        from: { x: -3000 },
        to: { x: 100 },
      })


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
              <h1>Product Name, Short Description of Program
                </h1></animated.div>
                </div>
                <div className="form-group">
                <form>
                  <label>Enter Your Flight Number <br />
                    <input name="flightnum" placeholder='Ex. DAL748'/>
                  </label>
                  <button type='submit' onClick={request.get('http://google.com/')}>Submit</button>
                </form>
          
            </div>
        </div>
        </>
    )
}

export default Home
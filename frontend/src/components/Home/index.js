import './index.scss';
import Sidebar from '../Sidebar';
import { Outlet } from 'react-router-dom'
import Layout from '../Layout';

import { useSpring, animated } from '@react-spring/web'

const Home = () => {
    const springs = useSpring({
        from: { x: 0 },
        to: { x: 100 },
      })

    return (
            

            <><Layout /><div className='container home-page'>
            <div className='text-zone'>
            <animated.div
            style={{
              width: 250,
              height: 500,
              borderRadius: 8,
              ...springs,
            }}
          ><h1>Product Name, SHort Description of Prigram
                </h1></animated.div>
            </div>
            
        </div>
        </>
    )
}

export default Home
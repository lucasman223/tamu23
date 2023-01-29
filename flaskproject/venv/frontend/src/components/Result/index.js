import './index.scss'
import Layout from '../Layout';
import { useTrail, useSpring, animated } from '@react-spring/web'

const Result = () => 
{
    const [trails, api] = useTrail(
        2,
        () => ({
          from: { opacity: 0 },
          to: { opacity: 1 },
        }),
        []
      )
      const springs = useSpring({
        from: { x: 0 },
        to: { x:  950},
      })

    return (
        <><Layout/><div className='container result-page'>
        {trails.map(props => (
        <animated.div style={props}>
        <div className='percent-zone'>
            <h1>10/10</h1>
        </div>
        <div className='text-zone'>Risk of <br /> Delay/Cancellation
        </div>
        </animated.div>))}
        
        <animated.div
            style={{
              width: 500,
              height: 750,
              borderRadius: 80,
              ...springs,
            }}>
        <div className='bullet-zone'>
          BUllet point 1 dwdiwjidw dwi diw diwdiw diw diwdwid <br />
          BUllet point 2  dw od wo owo wdow dowod wodwod<br />
          BUllet point 3 <br />
          BUllet point 4
        </div>
        </animated.div>
        
        </div>
        
        </>
    )
}

export default Result
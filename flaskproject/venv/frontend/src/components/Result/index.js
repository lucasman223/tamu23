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
            <h1>1/10</h1>
        </div>
        <div className='text-zone'>Risk of <br /> Delay/Cancellation <br/> for Flight 7945
        </div>
        <div className='rec-zone'>Recommended Flight: <br/> Flight 8501</div>

        </animated.div>))}
        
        <animated.div
            style={{
              width: 500,
              height: 750,
              borderRadius: 80,
              ...springs,
            }}>
        <div className='bullet-zone'>
          DFW <br />
          A slight chance of rain showers after noon. Mostly cloudy. High near 51, with temperatures falling to around 39 in the afternoon. <br />
          North northwest wind 10 to 15 mph, with gusts as high as 25 mph.<br />
          Chance of precipitation is 20%. <br /> <br/>
          PHL <br/>
          A chance of rain showers after 1pm. Cloudy, with a high near 52. <br/>
          Southwest wind 10 to 15 mph. Chance of precipitation is 30%.  <br/>
          New rainfall amounts less than a tenth of an inch possible.',<br/>
        </div>
        </animated.div>
        
        </div>
        
        </>
    )
}

export default Result
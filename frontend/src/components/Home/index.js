import './index.scss'
import Sidebar from '../Sidebar'
import { Outlet } from 'react-router-dom'

const Home = () => {
    return (
        <><Sidebar /><div className='container home-page'>
            <div className='text-zone'>
                <h1>Product Name, <br /> Enter <br /> your flight number
                </h1>
            </div>
        </div></>
    )
}

export default Home
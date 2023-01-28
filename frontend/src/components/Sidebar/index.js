import './index.scss'
import LogoP from '../../assets/LogoP.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome } from '@fortawesome/free-solid-svg-icons'


const Sidebar = () => (
    <div className='nav-bar'>
        <a href='/' className='logo'>
             <img src={LogoP} alt="logo" />
        </a>

    </div>

)

export default Sidebar
import './index.scss'
import LogoP from '../../assets/LogoP.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faUser } from '@fortawesome/free-solid-svg-icons'


const Sidebar = () => (
    <div className='nav-bar'>
        <a href='/' className='logo'>
             <img src={LogoP} alt="logo" />
        </a>
        
        <a href='/About' className='About'>
            <FontAwesomeIcon icon={faUser} color= "#4d4d4e" />
        </a>

    </div>

)

export default Sidebar
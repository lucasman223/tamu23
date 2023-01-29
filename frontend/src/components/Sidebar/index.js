import './index.scss'
import LogoP from '../../assets/LogoP.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faUser, faUserLarge } from '@fortawesome/free-solid-svg-icons'
import { faGithub } from '@fortawesome/free-brands-svg-icons'


const Sidebar = () => (
    <div className='nav-bar'>
        <a href='/' className='logo'>
             <img src={LogoP} alt="logo" />
        </a>
        
        <a href='/About' className='About'>
            <FontAwesomeIcon icon={faUserLarge} color= "#4d4d4e" />
        </a>

        <a href='https://github.com/lucasman223/tamu23' className='About'>
            <FontAwesomeIcon icon={faGithub} color= "#4d4d4e" />
        </a>
    </div>

)

export default Sidebar
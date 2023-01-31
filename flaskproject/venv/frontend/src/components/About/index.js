import './index.scss';
import React, {Fragment, useState} from 'react'
import cartoonplane from '../../assets/cartoonplane.jpg'


const About = () => {
    const [ toggleTab, setToggleTab] = useState()
    const toggleState = (index) =>{
        setToggleTab(index)
    }
    return (
        <Fragment>
            
            <section className="about">
 
                <div className="row">

                    <div className="column">

                        <div className="about-initial">
                                    <h2>Flight Forecast</h2>
                                    <p>This website allows a user to input a date and flight number and it will display a rating on the risk of the flight being delayed based on the a variety of factors.</p>
                                    <div>
                                        <img src={cartoonplane} alt="img" width={500} height={500}/>
                                    </div>
                        </div>
                    </div>
                    

                    <div className="column">
                        <div className="tabs">
                            <div className={toggleTab === 1 ? "single-tab active-tab": "single-tab"}
                            onClick = {() => toggleState(1)}>
                                <h2>Lucas</h2>
                            </div>
                            <div className={toggleTab === 2 ? "single-tab active-tab": "single-tab"}
                            onClick = {() => toggleState(2)}>
                                <h2>Andy</h2>
                            </div>
                            <div className={toggleTab === 3 ? "single-tab active-tab": "single-tab"}
                            onClick = {() => toggleState(3)}>
                                <h2>Kyumin</h2>
                            </div>
                            <div className={toggleTab === 4 ? "single-tab active-tab": "single-tab"}
                            onClick = {() => toggleState(4)}>
                                <h2>Austin</h2>
                            </div>
                        </div>
                        <div className="tab-content">
                            {/* About Content */}
                            <div className={toggleTab === 1 ? "content active-content" : "content"}>
                                <h2>Lucas Ma</h2>
                                <p>Class of '24 <br /> Computer Science <br /> Minor in Business <br /> lucaslma224@tamu.edu</p>
                            </div>
                            {/* Skills Content */}

                            <div className={toggleTab === 2 ? "content active-content" : "content"}>
                                <h2>Andy Wang</h2>
                                <p>Class of '22 <br /> Aerospace Engineer <br /> Minor in Math, Computer Science <br /> wa287142@tamu.edu </p>
                            </div>

                            {/* Experience Content */}
                            <div className={toggleTab === 3 ? "content active-content" : "content"}>

                            <h2>Kyumin Lee</h2>
                                <p>Class of '24 <br /> Applied Mathematics <br /> Computational Mathematics <br /> kevin5478233@tamu.edu </p>
                            </div>

                            <div className={toggleTab === 4 ? "content active-content" : "content"}>

                            <h2>Austin Ngo</h2>
                                <p>Class of '25 <br /> Electrical Engineer <br /> austingo@tamu.edu </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </Fragment>
    )
}

export default About


/*
export default function About() {
    return (
        <div className='container about-page'>
            <h1>About Page</h1>
            <div>
                this is random text
            </div>
        </div>
    )
}
*/
import React from "react";
import truck from "../truck.png"
import {fadeInLeftBig, fadeOutRightBig} from 'react-animations'
import styled, {keyframes} from 'styled-components'

const FadeInLeftBig = styled.div`animation: 2s ${keyframes`${fadeInLeftBig}`}`;
const FadeOutRightBig = styled.div`animation: 2s ${keyframes`${fadeOutRightBig}`}`;

export class Truck extends React.Component {
    render() {
        if (this.props.submitted === true) {
            return (

                <div className="container">
                    <FadeOutRightBig>
                        <div className="truck">
                            <img src={truck} className="truck-img" alt="truck" width={300}/>
                        </div>
                    </FadeOutRightBig>
                </div>
            )

        } else {
            return (
                <div className="container">
                    <FadeInLeftBig>
                        <div className="truck">
                            <img src={truck} className="truck-img" alt="truck" width={300}/>
                        </div>
                    </FadeInLeftBig>
                </div>
            )
        }


    }

}


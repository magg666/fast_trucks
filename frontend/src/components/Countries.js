import React from "react";
import {fadeIn} from 'react-animations'
import styled, {keyframes} from 'styled-components'
import {HiArrowRight} from "react-icons/hi";

const FadeIn = styled.div`animation: 2s ${keyframes`${fadeIn}`}`;

export class Countries extends React.Component {
    render() {
        return (
            <div className="container">
                <FadeIn>
                    <div>
                        {this.props.travel.map((via) => (

                            <span className='countries' key={via}><HiArrowRight/> {via}  </span>
                        ))}

                    </div>
                </FadeIn>
            </div>
        )
    }
}
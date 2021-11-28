import './App.css';
import React, {Component} from 'react';
import axios from 'axios'
import {FormSelect} from "./components/FormSelect";


class App extends Component {
    state = {countries: [], error: null}

    componentDidMount() {
        axios.get('https://fast-trucks-front-gw9ky.ondigitalocean.app/')
            .then(res => this.setState({countries: res.data}))
            .catch(error => this.setState({error}))
    }

    render() {
        return (
            <FormSelect allCountries={this.state.countries}/>
        )
    }
}

export default App;

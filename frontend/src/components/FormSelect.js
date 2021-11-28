import "../App.css"
import React from "react";
import {Field, Form, Formik, FormikProps} from 'formik';
import axios from 'axios'
import {Truck} from "./Truck";
import {Countries} from "./Countries";

export class FormSelect extends React.Component {
    state = {travel: [], error: null, isSubmitting: false}


    handleSubmit(resp) {
        this.setState({isSubmitting: true})
        if (resp.status === 200) {
            this.setState({travel: resp.data.countries})
            this.setState({error: resp.data.error})
        } else {
            this.setState({error: resp.data})
        }
    }

    render() {
        return (
            <div className='box'>
                <div className='container'>
                    <Formik initialValues={{start: '', end: ''}}
                            onSubmit={(values, {setSubmitting}) => {

                                setTimeout(() => {
                                    axios.post('https://fast-trucks-front-gw9ky.ondigitalocean.app/serve', {
                                        'start': values.start,
                                        'end': values.end
                                    })
                                        .then(res => this.handleSubmit(res))
                                        .catch(err => this.setState({error: err}))
                                }, 1000)
                                setSubmitting(false);
                            }}>
                        {(props: FormikProps<any>) => (
                            <Form>

                                    <Field as="select" name="start" className="custom-select" required>
                                        <option value="" label="Select start country"/>
                                        {this.props.allCountries.map((option) => (
                                            <option key={option.shortcut}
                                                    value={option.shortcut}>{option.country}</option>
                                        ))}
                                    </Field>

                                <Field as="select" name="end" className="custom-select"  required>

                                    <option value="" label="Select destination"/>
                                    {this.props.allCountries.map((option) => (
                                        <option key={option.shortcut} value={option.shortcut}>{option.country}</option>
                                    ))}
                                </Field>

                                <button type="submit" className="submit-button">Submit</button>
                            </Form>
                        )}
                    </Formik>
                </div>
                <Truck submitted={this.state.isSubmitting}/>
                <Countries travel={this.state.travel}/>
            </div>
        )
    }
}
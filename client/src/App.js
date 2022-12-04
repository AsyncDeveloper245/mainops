import React from "react"
import './App.css'

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {key: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({key: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    fetch(
      "http://localhost:5000", {
      method: 'post',
      body: JSON.stringify({"key":this.state.key}),
      headers: { 'Content-Type': 'application/json'},
    }
    ).then((res) => res.json()).then((data)=> console.log(data)).catch((err)=> console.log(err.text))
  }
 
  render() {
    return (
       <div className="App">
        <form onSubmit={this.handleSubmit}>
        < label for="key" className="labelkey">Key</label>
        <br/>
        <input className="key" value={this.state.key} onChange={this.handleChange} name="key"/>
        <hr/>
        <input type="submit" value='Get Encoded Value' onClick={this.handleSubmit}/>
        </form>
    </div>
    );
  }
}

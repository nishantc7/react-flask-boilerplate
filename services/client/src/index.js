import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import UsersList from './components/UsersList';

class App extends Component {

  constructor() {
    super();
    this.State = {
      users: []
    };
  };
  componentDidMount() {
    this.getUsers();
  }
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users }); })
    .catch((err) => {console.log(err);})
  
  }
  render() {
  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6">
          <br/>
          <h1>All Users</h1>
          <hr/><br/>
          <UsersList users={this.state.users}/>
        </div>
      </div>
    </div>
  )
    }
  

  
  
};


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

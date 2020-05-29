import React, { Component } from 'react'
import axios from 'axios'

import UsersList from './components/UsersList'
import AddUser from './components/AddUser'
import About from './components/About';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Switch, Route } from 'react-router-dom';



class App extends Component{
    constructor() {
        super();
        this.state = {
            users: [],
            username: '',
            email: '',
            password: '',

        };
        this.addUser = this.addUser.bind(this)
        this.handleChange = this.handleChange.bind(this)

    };
    componentDidMount() {
        this.getUsers();
    };
    getUsers() {
        axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
        .then((res) => { this.setState({ users: res.data.data.users }); })
        .catch((err) => { console.log(err); });
      };
      addUser(event) {
        event.preventDefault();
        const data = {
          username: this.state.username,
          email: this.state.email,
          password: this.state.password
        };
        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
        .then((res) => {
          this.getUsers();  // new
          this.setState({ username: '', email: '', password:''});  // new
        })
        .catch((err) => { console.log(err); });
      };
      handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
      };
      render() {
        return (
            <div className="container">
              <div className="columns">
                <div className="column is-half">
                  <br/>
                  <Switch>
                      <Route exact path='/' render={() => (
                          <div>
                    <h1 className="title is-1">All Users</h1>
                  <hr/><br/>
                  <AddUser
                    username={this.state.username}
                    email={this.state.email}
                    addUser={this.addUser}
                    handleChange={this.handleChange}
                  />
                  <br/><br/>
                  <UsersList users={this.state.users}/>
                  </div>
                  )}/>
                  <Route exact path='/about' component={About}/>
                </Switch>
                </div>
              </div>
            </div>
        )
      }
    };

export default App;
import App from '../../App';
import React from 'react';
import { shallow } from 'enzyme';


test('App renders without crashing', () => {
    const wrapper = shallow(<App/>);
    });
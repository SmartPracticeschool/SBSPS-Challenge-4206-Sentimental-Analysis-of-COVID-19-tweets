import React, { useState, useEffect } from 'react';
import { Layout, Menu } from 'antd';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';
import { urls } from '../constants';

const { Header, Content } = Layout;

const CustomLayout = props => {
  const [homeSelectedKey, setHomeSelectedKey] = useState([]);
  useEffect(() => {
    if (props.location.pathname === "/") {
      setHomeSelectedKey(["1"]);
    } else if (props.location.pathname === "/analysis") {
      setHomeSelectedKey(["2"]);
    } else if (props.location.pathname === "/login") {
      setHomeSelectedKey(["5"]);
    }

    if (props.isAuthenticated && (props.location.pathname === "/login" || props.location.pathname === "signup")) {
      props.history.push('/analysis');
    } else if (!props.isAuthenticated && (props.location.pathname.split('/')[1] === "analysis")) {
      props.history.push('/login');
    }
  }, [props]);
  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" selectedKeys={homeSelectedKey}>
          {
            props.isAuthenticated ?
              null
              :
              <Menu.Item style={{ float: 'right' }} key="4"><a href={`${urls.baseUrl}admin/`}>Admin Panel</a></Menu.Item>
          }
          <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
          {
            props.isAuthenticated ?
              <Menu.Item key="2"><Link to="/analysis">My Analysis</Link></Menu.Item>
              :
              null
          }
          {
            props.isAuthenticated ?
              <Menu.Item style={{ float: 'right' }} key="3" onClick={props.logout}>Logout</Menu.Item>
              :
              <Menu.Item key="5"><Link to="/login">Login</Link></Menu.Item>
          }
        </Menu>
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <div className="site-layout-content">
          <div style={{
            display: 'flex',
            flex: 1,
            marginTop: 30,
            alignItems: 'center',
            justifyContent: 'center',
          }}>
            {props.children}
          </div>
        </div>
      </Content>
    </Layout>
  );
};

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(actions.logout())
  };
};

export default withRouter(connect(null, mapDispatchToProps)(CustomLayout));
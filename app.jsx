import React from 'react';

import { ConfigApi } from './api.js';
import "./app.scss";


export default class App extends React.Component
{
    constructor(props)
    {
	super(props);
	this.state = {
	    configs: []
	};
	this.config_api = new ConfigApi();
	this.refresh_configs = this.refresh_configs.bind(this);
	this.create_config = this.create_config.bind(this);
	this.delete_config = this.delete_config.bind(this);
    }

    componentDidMount()
    {
	this.refresh_configs();
    }

    refresh_configs()
    {
	this.config_api.get_configs().then(
	    data => {
		if(data.success) {
		    this.setState({configs: data.data});
		}
	    }
	);
    }

    filter_config()
    {
    }

    create_config()
    {
	this.config_api.create_config({
	    config_name: this.refs.cname.value,
	    config_type: this.refs.ctype.value,
	    config_value: this.refs.cvalue.value
	}).then(
	    data => {
		console.log(data);
	    }
	);
    }

    delete_config(config_name)
    {
	this.config_api.delete_config([config_name]).then(
	    data => console.log(data)
	);
    }

    render()
    {
	return (
	    <div className="body">
	        <div className="config-panel">
	           <div className="cp-header">
	               <input disabled placeholder="Please enter config name"/>
	               <button disabled onClick={this.filter_config}>Search</button>
	               <div className="flex-right">
	                   <button onClick={this.refresh_configs}>Refresh</button>
	               </div>
	           </div>
	           <div className="cp-body">
                       <table border="1" width="100%">
	                   <tbody>
	                       {this.state.configs.map(
				   (config, idx) => {
				       return (
					   <tr key={`c-${idx}`}>
					       <td>{config.config_name}</td>
					       <td>{config.config_type}</td>
					       <td>{config.config_value}</td>
					       <td><button onClick={() => this.delete_config(config.config_name)}>Delete</button></td>
					   </tr>
				       );
				   }
			       )}
	                   </tbody>
	               </table>
	           </div>
	           <div className="cp-footer">
	               <input ref="cname" placeholder="Config name"/>
	               <input ref="ctype" placeholder="Config type"/>
	               <input ref="cvalue" placeholder="Config value"/>
	               <div className="flex-right">
	                   <button onClick={this.create_config}>Create</button>
	               </div>
	           </div>
	        </div>
	    </div>
	);
    }
}

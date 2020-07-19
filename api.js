import config from './config.json';


class ConfigApi
{
    get base_url()
    {
	return config.base_url;
    }

    jres({url, options})
    {
	return new Promise(
	    (resolve, reject) => {
		fetch(url, options).then(
		    response => response.json()
		).then(
		    json_data => resolve(json_data)
		).catch(err => reject(err))
	    }
	);
    }

    get_configs()
    {
	return this.jres({url: `${this.base_url}/config`, options: {}});
    }

    get_config(config_name)
    {
	return this.jres({url: `${this.base_url}/config?config_name=${config_name}`, options: {}});
    }

    create_config({ config_name, config_type, config_value })
    {
	return this.jres({
	    url: `${this.base_url}/config`,
	    options: {
		body: JSON.stringify({
		    config_name: config_name,
		    config_type: config_type,
		    config_value: config_value
		}),
		method: "POST",
		headers: {
		    "Content-Type": "application/json"
		}
	    }
	});
    }

    update_config({config_name, config_type, config_value})
    {
	return this.jres({
	    url: `${this.base_url}/config`,
	    options: {
		body: JSON.stringify({
		    config_name: config_name,
		    config_type: config_type,
		    config_value: config_value
		}),
		method: "PUT",
		headers: {
		    "Content-Type": "application/json"
		}
	    }
	});
    }

    delete_config(config_names)
    {
	return this.jres({
	    url: `${this.base_url}/config`,
	    options: {
		body: JSON.stringify({
		    config_names: config_names,
		}),
		method: "DELETE",
		headers: {
		    "Content-Type": "application/json"
		}
	    }
	});
    }
}


export {
    ConfigApi
};

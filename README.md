# hmc-controller


## creating the .env

Your `.env` file should look like this:

```env
LXD_API=https://<ip>:8443
LXD_CRT=<path>
LXD_KEY=<path>
KUBE_CONFIG=<path>
OPENFAAS_API=<openfaas_url>
```

## Endpoints

- `/` Root
- `/health` Health of services
- `/api` Endpoints
- `/api/functions` Get / Create functions
- `/api/functions/{name}` Get / Delete / Execute funtion
- `/api/iaas` Get / Create IaaS
- `/api/iaas/{name}` Get / Delete IaaS
- `/api/iaas/{name}/instances` Get / Create Instances
- `/api/iaas/{name}/instances/{name}` Get / Delete Instance
- `/api/iaas/{name}/instances/{name}/actions` Get / shell / forward on Instance
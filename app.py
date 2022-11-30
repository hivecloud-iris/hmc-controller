from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    """Get health of all services"""
    return {"services": {"hmc-k8s": "<health>", "hmc-cr": "<health>", "hmc-pi": "<health>"}}

@app.get("/api")
async def api():
    """Get endpoints"""
    return

@app.get("/api/functions")
async def get_funcs():
    """List all functions"""
    return

@app.post("/api/functions")
async def create_func():
    """Create a function"""
    return

@app.delete("/api/functions/{name}")
async def delete_func():
    """Delete a function"""
    return

@app.get("/api/functions/{name}")
async def get_func():
    """Get a function's information"""
    return

# ------------IAAS------------------
@app.get("/api/iaas")
async def get_all_iaas():
    """List all IaaS"""
    return

@app.post("/api/iaas")
async def create_iaas():
    """Create an IaaS"""
    return

@app.delete("/api/iaas/{name}")
async def delete_iaas():
    """Delete an IaaS"""
    return

@app.get("/api/iaas/{name}")
async def get_iaas():
    """Get an IaaS information"""
    return

@app.get("/api/iaas/{name}/instances")
async def get_iaas_instances():
    """Get all instances in an IaaS"""
    return

@app.post("/api/iaas/{name}/instances")
async def create_iaas_instance():
    """Create an instances in a IaaS"""
    return

@app.delete("/api/iaas/{name}/instances/{name}")
async def delete_iaas_instance():
    """Delete an instances in a IaaS"""
    return

@app.get("/api/iaas/{name}/instances/{name}")
async def get_iaas_instances():
    """Get instances information in an IaaS"""
    return

@app.get("/api/iaas/{name}/instances/{name}/actions")
async def get_actions():
    """Get all actions for instance"""
    return

@app.post("/api/iaas/{name}/instances/{name}/actions")
async def exec_action():
    """execute actions on instance"""
    return
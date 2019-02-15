import json, falcon, hashlib


# Authentication Information
auth = {
    "641daba7-447a-4531-83a9-0c1edf44dfca": {
        "user": "jaykepeters",
        "allowed_hosts": ["0.0.0.0/0"],
        "max_requests": 120
    }
}
class defaultRequest:
    def on_get(self, req, resp):
        if 'APIKEY' not in req.params:
            response = {"error": "INVALID API KEY"}
            resp.status = falcon.HTTP_400
        else:
            if req.params['APIKEY'] != APIKEY:
                response = {"error": "INVALID API KEY"}
                resp.status = falcon.HTTP_400
            else:
                response = {
                    "URI": req.uri,
                    "Method": req.method,
                    "status": resp.status,
                    "parameters": req.params,
                    "Client IP": req.remote_addr,
                    "User Agent": req.user_agent
                }
                resp.status = falcon.HTTP_200
                # add ip and get valids from databased based on key...
                resp.set_header("Access-Control-Allow-Origin", "*")
                resp.append_header("cache_control", '0')
        # DUMP THE RESPONSE
        resp.body = json.dumps(response)


    def on_post(self, req, resp):
        resp.body = json.dumps(req.stream.read())

api = falcon.API()
api.add_route("/stats", defaultRequest())


# use the IPaddress module to check if the IP is allowed to access, log the attempts too...

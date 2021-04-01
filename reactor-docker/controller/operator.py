from flask import Flask, request
app = Flask(__name__)


class Server:
    reactor = None
    def __init__(self, reactor):
        Server.reactor = reactor



    @staticmethod
    @app.route('/')
    def index():
        return 'Nuclear rector page'

    @staticmethod
    @app.route('/api/controlrods', methods=["GET"])
    def get_control_rods():
        return {"rod_state": Server.reactor.rods}

    """
    set control rods by value
    """
    @staticmethod
    @app.route('/api/controlrods/<int:value>', methods=["POST"])
    def set_control_rods_by_url(value):
        rods = value
        Server.reactor.rods = rods
        return {"rod_state": Server.reactor.rods}


    @staticmethod
    @app.route("/api/controlrods", methods=["POST"])
    def starting_url():
        json_data = request.json
        rod_state = json_data["rod_state"]
        Server.reactor.rods = rod_state
        return {"control_rod_set: ": Server.reactor.rods}

    """
    set control rods by 100 (AZ-5)
    """

    @staticmethod
    @app.route('/api/az-5', methods=["POST"])
    def az_5_rod():
        rods = 100
        Server.reactor.rods = rods
        return {"rod_state": Server.reactor.rods}

    """
    check temperature of the nuclear reactor at now
    """

    @staticmethod
    @app.route('/api/checktemperature', methods=["GET"])
    def get_check_temperature():
        return {"temperature": Server.reactor.temperature}

    """
    get all of the datas about the nuclear reactor
    """

    @staticmethod
    @app.route('/api/reactor_status', methods=["GET"])
    def get_reactor_datas():
        return {
            "uran235": Server.reactor.uran235,
            "split": Server.reactor.split,
            "xenon": Server.reactor.xenon,
            "xenon_start": Server.reactor.xenon_start,
            "temperature": Server.reactor.temperature,
            "temperature_start": Server.reactor.temperature_start,
            "rods": Server.reactor.rods,
            "produce": Server.reactor.produce,
            "water": Server.reactor.water,
            "steam": Server.reactor.steam,
            "counter": Server.reactor.counter,
            "operate": Server.reactor.operate
        }

    """
    start the reactor
    """

    @staticmethod
    @app.route('/api/start_reactor', methods=["POST"])
    def start_reactor():
        operate = True
        Server.reactor.operate = operate
        return {"reactor started": Server.reactor.operate}

    @staticmethod
    @app.route('/api/stop_reactor', methods=["POST"])
    def stop_reactor():
        operate = False
        Server.reactor.operate = operate
        return {"reactor started": Server.reactor.operate}


    def run_web_app(self, port=1986):
        app.run(port=port)
        print("server is running on port" + port)


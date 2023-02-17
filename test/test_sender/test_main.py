from src.sender.main import main

class DummyLogger():
    def __init__(self):
        self.data = []

    def log(self, logs):
        self.data.append(logs)



def test_main_with_single_stream():
    logger = DummyLogger()
    main(logger,1)
    stored_data = logger.data[0]
    assert(type(stored_data) == dict)
    assert(len(stored_data["charge_rate"]) == 50)
    assert(len(stored_data["temperature"]) == 50)


def test_main_with_multiple_streams():
    logger = DummyLogger()
    main(logger,10)
    stored_data = logger.data
    assert(len(stored_data) == 10)

